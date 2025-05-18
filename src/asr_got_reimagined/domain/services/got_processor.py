import time
import uuid
from typing import Any, Dict, List, Optional, Type

from loguru import logger
from pydantic import BaseModel, Field

from asr_got_reimagined.domain.models.graph_state import ASRGoTGraph
from asr_got_reimagined.domain.stages.base_stage import BaseStage


class GoTProcessorSessionData(BaseModel):
    """Data model for session data maintained by GoTProcessor."""

    session_id: str = Field(default_factory=lambda: f"session-{uuid.uuid4()}")
    query: str
    graph_state: Optional[ASRGoTGraph] = None
    final_answer: Optional[str] = None
    final_confidence_vector: List[float] = Field(default=[0.5, 0.5, 0.5, 0.5])
    accumulated_context: Dict[str, Any] = Field(default_factory=dict)
    stage_outputs_trace: List[Dict[str, Any]] = Field(default_factory=list)


class ComposedOutput(BaseModel):
    """Model for the output structure from the Composition Stage."""

    executive_summary: str
    detailed_report: Optional[str] = None
    key_findings: List[str] = Field(default_factory=list)
    confidence_assessment: Optional[Dict[str, Any]] = None


class GoTProcessor:
    def __init__(self, settings):
        self.settings = settings
        logger.info("Initializing GoTProcessor")

    def _initialize_stages(self) -> List[BaseStage]:
        """Dynamically loads and initializes all stage classes."""
        from asr_got_reimagined.domain.stages import (
            CompositionStage,
            DecompositionStage,
            EvidenceStage,
            HypothesisStage,
            InitializationStage,
            PruningMergingStage,
            ReflectionStage,
            SubgraphExtractionStage,
        )

        # All stages are now real implementations
        stages_to_load: List[Type[BaseStage]] = [
            InitializationStage,
            DecompositionStage,
            HypothesisStage,
            EvidenceStage,
            PruningMergingStage,
            SubgraphExtractionStage,
            CompositionStage,
            ReflectionStage,
        ]

        initialized_stages = [stage_cls(self.settings) for stage_cls in stages_to_load]

        if len(initialized_stages) != 8:
            logger.warning(
                f"Expected 8 stages, but only {len(initialized_stages)} were initialized. Check _initialize_stages."
            )

        return initialized_stages

    async def process_query(
        self,
        query: str,
        session_id: Optional[str] = None,
        operational_params: Optional[Dict[str, Any]] = None,
        initial_context: Optional[Dict[str, Any]] = None,
    ) -> GoTProcessorSessionData:
        """
        Process a natural language query through the ASR-GoT stages.

        Args:
            query: The natural language query to process
            session_id: Optional session ID to continue or manage a session
            operational_params: Optional parameters to control the processing behavior
            initial_context: Optional initial context to seed the processing

        Returns:
            GoTProcessorSessionData: The result of processing the query
        """
        from asr_got_reimagined.domain.stages import CompositionStage, ReflectionStage

        start_total_time = time.time()
        logger.info(f"Starting NexusMind query processing for: '{query[:100]}...'")

        # Initialize or retrieve session data
        current_session_data = GoTProcessorSessionData(
            session_id=session_id or f"session-{uuid.uuid4()}", query=query
        )

        # Create a new graph state for this session
        current_session_data.graph_state = ASRGoTGraph()
        current_session_data.graph_state.graph_metadata["query"] = query
        current_session_data.graph_state.graph_metadata["session_id"] = (
            current_session_data.session_id
        )

        # Process initial context
        if initial_context:
            current_session_data.accumulated_context["initial_context"] = (
                initial_context
            )

        # Process operational parameters
        op_params = operational_params or {}
        current_session_data.accumulated_context["operational_params"] = op_params

        # Execute stages in sequence
        stages = self._initialize_stages()
        logger.info(f"Initialized {len(stages)} processing stages")

        for i, stage in enumerate(stages):
            stage_start_time = time.time()
            stage_name = stage.__class__.__name__
            logger.info(f"Executing stage {i + 1}/{len(stages)}: {stage_name}")

            try:  # Execute the stage
                stage_result = await stage.execute(
                    graph=current_session_data.graph_state,
                    current_session_data=current_session_data,
                )

                # Update session data with stage results
                if stage_result:
                    current_session_data.accumulated_context[stage.stage_name] = (
                        stage_result
                    )

                # Record stage execution in trace
                stage_duration_ms = int((time.time() - stage_start_time) * 1000)
                trace_entry = {
                    "stage_number": i + 1,
                    "stage_name": stage_name,
                    "duration_ms": stage_duration_ms,
                    "summary": f"Completed {stage_name}",
                }
                current_session_data.stage_outputs_trace.append(trace_entry)

                logger.info(
                    f"Completed stage {i + 1}: {stage_name} in {stage_duration_ms}ms"
                )

            except Exception as e:
                logger.error(f"Error in stage {i + 1} ({stage_name}): {e!s}")
                trace_entry = {
                    "stage_number": i + 1,
                    "stage_name": stage_name,
                    "error": str(e),
                    "summary": f"Error in {stage_name}: {e!s}",
                }
                current_session_data.stage_outputs_trace.append(trace_entry)
                # Continue to next stage despite errors

        # Extract final answer from composition stage
        composition_stage_output_key = CompositionStage.stage_name
        final_composed_output_dict = current_session_data.accumulated_context.get(
            composition_stage_output_key, {}
        ).get("final_composed_output")

        if final_composed_output_dict:
            try:
                final_output_obj = ComposedOutput(**final_composed_output_dict)
                current_session_data.final_answer = f"{final_output_obj.executive_summary}\n\n(Full report details generated)"
            except Exception as e:
                logger.error(
                    f"Could not parse final_composed_output from CompositionStage: {e}"
                )
                current_session_data.final_answer = (
                    "Error during final composition of answer."
                )
        else:
            current_session_data.final_answer = (
                "Composition stage did not produce a final output structure."
            )

        # Get final confidence from ReflectionStage's output
        reflection_stage_output_key = ReflectionStage.stage_name
        reflection_output = current_session_data.accumulated_context.get(
            reflection_stage_output_key, {}
        )
        current_session_data.final_confidence_vector = reflection_output.get(
            "final_confidence_vector_from_reflection",
            [0.1, 0.1, 0.1, 0.1],  # Low default if not found
        )

        total_execution_time_ms = int((time.time() - start_total_time) * 1000)
        logger.info(
            f"NexusMind query processing completed for session {current_session_data.session_id} in {total_execution_time_ms}ms."
        )

        return current_session_data

    async def shutdown_resources(self):
        """Clean up any resources when shutting down."""
        logger.info("Shutting down GoTProcessor resources")
        # Close any connections, release resources, etc.
        return
