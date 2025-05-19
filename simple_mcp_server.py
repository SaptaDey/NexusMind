from fastapi import FastAPI, Request
import uvicorn
from pydantic import BaseModel
from typing import Dict, Any, Optional, List, Union
import json

app = FastAPI()

class QueryContext(BaseModel):
    conversation_id: Optional[str] = None
    history: Optional[List[Dict[str, Any]]] = None
    user_preferences: Dict[str, Any] = {}

class QueryParams(BaseModel):
    query: str
    context: Optional[QueryContext] = None
    parameters: Optional[Dict[str, Any]] = None
    session_id: Optional[str] = None

class RequestParams(BaseModel):
    jsonrpc: str = "2.0"
    method: str
    id: Union[str, int]
    params: Dict[str, Any]

@app.post("/mcp")
async def mcp_handler(request: Request):
    try:
        data = await request.json()
        jsonrpc = data.get("jsonrpc")
        method = data.get("method")
        req_id = data.get("id")
        params = data.get("params", {})

        print(f"Received MCP request: {method}, id: {req_id}")
        print(f"Params: {json.dumps(params, indent=2)}")

        if method == "initialize":
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {
                    "server_name": "NexusMind MCP Server",
                    "server_version": "0.1.0",
                    "mcp_version": "2024-11-05"
                }
            }
        elif method == "asr_got.query":
            query = params.get("query", "No query provided")
            # Simulate detailed response with reasoning traces and graph states
            reasoning_trace_summary = "Reasoning trace: Step 1 -> Step 2 -> Step 3"
            graph_state_full = {
                "nodes": [
                    {"id": "n1", "label": "Node 1", "type": "root"},
                    {"id": "n2", "label": "Node 2", "type": "evidence"}
                ],
                "edges": [
                    {"id": "e1", "source": "n1", "target": "n2", "type": "supports"}
                ]
            }
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {
                    "answer": f"NexusMind processed your query: {query}",
                    "reasoning_trace_summary": reasoning_trace_summary,
                    "graph_state_full": graph_state_full,
                    "confidence_vector": [0.85, 0.92, 0.78, 0.89],
                    "execution_time_ms": 1250,
                    "session_id": "sample-session-123"
                }
            }
        elif method == "shutdown":
            return {
                "jsonrpc": "2.0", 
                "id": req_id,
                "result": None
            }
        else:
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "error": {
                    "code": -32601,
                    "message": f"Method '{method}' not supported"
                }
            }
    except Exception as e:
        return {
            "jsonrpc": "2.0",
            "id": None,
            "error": {
                "code": -32603,
                "message": f"Internal error: {str(e)}"
            }
        }

@app.get("/health")
async def health_check():
    return {"status": "healthy", "version": "0.1.0"}

if __name__ == "__main__":
    print("Starting NexusMind MCP Server...")
    uvicorn.run(app, host="0.0.0.0", port=8000)
