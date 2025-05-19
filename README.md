# 🧠 NexusMind

<div align="center">

<img src="https://raw.githubusercontent.com/SaptaDey/NexusMind/main/static/nexusmind-logo.png" width="180" height="180" alt="NexusMind Logo"/>

#### **Intelligent Scientific Reasoning through Graph-of-Thoughts**

[![Version](https://img.shields.io/badge/version-0.1.0-blue.svg)](https://github.com/SaptaDey/NexusMind/releases)
[![Python](https://img.shields.io/badge/python-3.13.3-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-Apache_2.0-green.svg)](LICENSE)
[![Docker](https://img.shields.io/badge/docker-ready-brightgreen.svg)](Dockerfile)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.111.0-009688.svg)](https://fastapi.tiangolo.com)
[![NetworkX](https://img.shields.io/badge/NetworkX-3.3-orange.svg)](https://networkx.org)
[![Last Updated](https://img.shields.io/badge/last_updated-May_2025-lightgrey.svg)](CHANGELOG.md)

</div>

<div align="center">
  <p><strong>🚀 Next-Generation AI Reasoning Framework for Scientific Research</strong></p>
  <p><em>Leveraging graph structures to transform how AI systems approach scientific reasoning</em></p>
</div>

## 🔍 Overview

NexusMind leverages **graph structures** to perform sophisticated scientific reasoning. It implements the **Model Context Protocol (MCP)** to integrate with AI applications like Claude Desktop.

**Key highlights:**
- Process complex scientific queries using graph-based reasoning
- Dynamic confidence scoring with multi-dimensional evaluations 
- Built with modern Python and FastAPI for high performance
- Dockerized for easy deployment
- Modular design for extensibility and customization

## 🌟 Key Features

### 8-Stage Reasoning Pipeline

<div align="center">
  <img src="https://mermaid.ink/img/pako:eNqNk01PwzAMhv9KlBNIaIhtt1UwDhw2cUCIw5K4W9HSlI6kGkP03zMnLSsVA3GJneTxm8_XnUhuGFeFmPgtKty6NcuXCih6p9oonN9SPuoK9ch7dJynwKhanBYNKZHN8BOcx8CerrEsuzG8o3a1PmnUx-BwTQbpvnfnHRqsrWvPqbMmCPJduueDJG74XWnUe00PrK1-z1pInILbI7vzYULl7MBujNP-jOR6JCZ9QfbONP-Gobhle9rGNX3FrmftWYMzx71Q5fCJrGwrZqvEJRg0LehQeey4St8ZkefoaHH6VvM09XN6wfvkKeWITc75sLzLJ0smaNQdq0piR_jFaTuioiHe8SS_tvlPkhPIST1Q3TgfTF8N20PP-4fp-49VqM9Rt45PeJpfYMrTBbycNj6j27Hp4d4P58J_6Wh2Hw_O5vP5jDeHvZUz4-9BGqbIb_SUiZk4pPFmcsS6p7Emf1anBR-eUaepSQuXs45HRYr2AkojCNR-aDzoaLkZA2JZezapw5YSZ6zMcePcY0yaBWUIx0XJCfraMVgBDQq5RQNKSseKnS_KptPwVYZ6PMH9IVwun83a2-KZ69SPk_wFo9Vg_w?type=png" width="700" height="400"/>
</div>

The core reasoning process follows a sophisticated 8-stage pipeline:

1. **🌱 Initialization**
   - Creates root node from query
   - Establishes initial graph structure
   - Sets confidence baseline

2. **🧩 Decomposition**
   - Breaks query into dimensions
   - Identifies key components
   - Creates dimensional nodes

3. **🔬 Hypothesis/Planning**
   - Generates multiple hypotheses
   - Creates reasoning strategy
   - Establishes falsification criteria

4. **📊 Evidence Integration**
   - Gathers supporting evidence
   - Links evidence to hypotheses
   - Updates confidence scores

5. **✂️ Pruning/Merging**
   - Removes low-value elements
   - Consolidates similar nodes
   - Optimizes graph structure

6. **🔍 Subgraph Extraction**
   - Identifies relevant portions
   - Focuses on high-value paths
   - Creates targeted subgraphs

7. **📝 Composition**
   - Synthesizes key findings
   - Creates coherent insights
   - Generates comprehensive answer

8. **🤔 Reflection**
   - Evaluates reasoning quality
   - Identifies improvement areas
   - Final confidence assessment

### Technical Capabilities

<div align="center">
  <table>
    <tr>
      <td align="center">🔄 <b>Multi-Dimensional<br>Confidence</b></td>
      <td align="center">🧠 <b>Graph-Based<br>Knowledge</b></td>
      <td align="center">🔌 <b>MCP<br>Integration</b></td>
      <td align="center">⚡ <b>FastAPI<br>Backend</b></td>
    </tr>
    <tr>
      <td align="center">🐳 <b>Docker<br>Deployment</b></td>
      <td align="center">🧩 <b>Modular<br>Design</b></td>
      <td align="center">⚙️ <b>Configuration<br>Management</b></td>
      <td align="center">🔒 <b>Type<br>Safety</b></td>
    </tr>
  </table>
</div>

- **🧠 Graph Knowledge Representation**: Uses `networkx` to model complex relationships
- **🔄 Dynamic Confidence Vectors**:
  - Empirical support
  - Theoretical basis
  - Methodological rigor
  - Consensus alignment
- **🔌 MCP Server**: Seamless Claude Desktop integration
- **⚡ High-Performance API**: Modern FastAPI implementation
- **🐳 Easy Deployment**: Docker & Docker Compose support
- **🧩 Extensible Architecture**: Modular components for customization
- **⚙️ Flexible Configuration**: Pydantic & YAML configuration

## 🛠️ Technology Stack

<div align="center">
  <table>
    <tr>
      <td align="center"><img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" width="38" height="38"/><br>Python 3.13+</td>
      <td align="center"><img src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" width="38" height="38"/><br>FastAPI</td>
      <td align="center"><img src="https://networkx.org/documentation/stable/_static/networkx_logo.svg" width="38" height="38"/><br>NetworkX</td>
      <td align="center"><img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/docker/docker-original.svg" width="38" height="38"/><br>Docker</td>
    </tr>
    <tr>
      <td align="center"><img src="https://docs.pytest.org/en/7.3.x/_static/pytest_logo_curves.svg" width="38" height="38"/><br>Pytest</td>
      <td align="center"><img src="https://docs.pydantic.dev/latest/img/logo-white.svg" width="38" height="38"/><br>Pydantic</td>
      <td align="center"><img src="https://python-poetry.org/images/logo-origami.svg" width="38" height="38"/><br>Poetry</td>
      <td align="center"><img src="https://raw.githubusercontent.com/tomchristie/uvicorn/master/docs/uvicorn.png" width="38" height="38"/><br>Uvicorn</td>
    </tr>
  </table>
</div>

## 📂 Project Structure

```
asr-got-reimagined/
├── config/                        
│   ├── settings.yaml              
│   └── claude_mcp_config.json     
├── src/asr_got_reimagined/        
│   ├── api/                       
│   │   ├── routes/                
│   │   │   └── mcp.py             
│   │   └── schemas.py             
│   ├── domain/                    
│   │   ├── models/                
│   │   │   ├── common.py          
│   │   │   ├── graph_elements.py  
│   │   │   └── graph_state.py     
│   │   ├── services/              
│   │   │   └── got_processor.py   
│   │   ├── stages/                
│   │   │   ├── base_stage.py      
│   │   │   ├── stage_1_*.py       
│   │   │   └── stage_2_*.py...    
│   │   └── utils/                 
│   ├── main.py                    
│   └── app_setup.py               
├── scripts/                       
├── Dockerfile                     
├── docker-compose.yml             
└── pyproject.toml                 
```

## 🚀 Getting Started

### Prerequisites

- **Python 3.13+** (Docker image uses Python 3.13.3-slim-bookworm)
- **[Poetry](https://python-poetry.org/docs/#installation)**: For dependency management
- **[Docker](https://www.docker.com/get-started)** and **[Docker Compose](https://docs.docker.com/compose/install/)**: For containerized deployment

### Installation and Setup (Local Development)

1. **Clone the repository**:
   ```bash
   git clone https://github.com/SaptaDey/NexusMind.git
   cd NexusMind
   ```

2. **Install dependencies using Poetry**:
   ```bash
   poetry install
   ```
   This creates a virtual environment and installs all necessary packages specified in `pyproject.toml`.

3. **Activate the virtual environment**:
   ```bash
   poetry shell
   ```

4. **Configure the application**:
   - Adjust settings in `config/settings.yaml` as needed
   - Configure environment variables or a `.env` file for sensitive information

5. **Run the development server**:
   ```bash
   python src/asr_got_reimagined/main.py
   ```
   
   Alternatively, for more control:
   ```bash
   uvicorn asr_got_reimagined.main:app --reload --host 0.0.0.0 --port 8000
   ```
   
   The API will be available at `http://localhost:8000`.

### Docker Deployment

<div align="center">
  <img src="https://mermaid.ink/img/pako:eNptks1uwjAMx1_FyglQaAjYbmXqgcPGpk2bog1xaWLXmibOlLhQNeW9Z5C2AuWQyPb_Z8ef5B2VXiKvxD1KfMfDw4wNGyWZqqywIH1R4X6y6Gaj5SN4TorF0j_qyNXOJvlm9FLp4CyJA5DxXDcmzrYmFHhNnHpML0_Yo9fzmmI0Ojnrr1AHn-wNdB_VB89_nj6ez5qNohb8I3Gla3ZmbuVdP2LOeI_Df54ttWQtfuG6h21wj-xcaNfRP41wG2fr5Qa8zdn6o89GRb_5nmR8_RC6VrJHUdSTzJXRLBHodCGurhSTJu6mRCmneZlG6WyVJpNxnrH7aclub5dhGK_ydDrJ43zCTscylUn--hfwPK_APAsGGcj2AG7J-0l8Bgc5bYjkU2jO1rRruBhtKLgxP2jRguKMuabZ_ohUsq2hf3FXw3xEv3ic4n4XUD_Tan-7GhQK6fFSuCeD0hTSKAykFEdSjoXKmZSIzbnCfKcc7V9zfX5-pbm41Z-kdTVLXA?type=png" width="500" height="300"/>
</div>

1. **Build and run the Docker containers**:
   ```bash
   docker-compose up --build
   ```
   
   For detached mode:
   ```bash
   docker-compose up --build -d
   ```
   
   The Docker image uses Python 3.13.3-slim-bookworm as the base image for improved performance and security.

2. **Access the API**:
   The API will be accessible at `http://localhost:8000` (or as configured in `docker-compose.yml`).

## 🔌 API Endpoints

### Core Endpoints

- **MCP Endpoint**: `POST /mcp`
  - For communication with MCP clients like Claude Desktop
  - Implements the Model Context Protocol for AI interaction

- **Health Check**: `GET /health`
  - Basic health check for monitoring and service discovery

### Additional Endpoints (Planned)

- **Graph Query**: `POST /api/graph/query`
  - Direct interface for ASR-GoT queries
  
- **Graph State**: `GET /api/graph/{session_id}`
  - Retrieve current state of a reasoning graph

- **Analytics**: `GET /api/analytics/{session_id}`
  - Get metrics about the reasoning process

## 🧪 Testing & Quality

<div align="center">
  <table>
    <tr>
      <td align="center">🧪<br><b>Testing</b></td>
      <td align="center">🔍<br><b>Type Checking</b></td>
      <td align="center">✨<br><b>Linting</b></td>
    </tr>
    <tr>
      <td align="center">
        <pre>poetry run pytest</pre>
        <pre>poetry run pytest --cov=src</pre>
      </td>
      <td align="center">
        <pre>poetry run mypy src/</pre>
        <pre>pyright src/</pre>
      </td>
      <td align="center">
        <pre>poetry run ruff check .</pre>
        <pre>poetry run ruff format .</pre>
      </td>
    </tr>
  </table>
</div>

### Development Tools

- **Type Safety**: 
  - Configured with `mypy.ini` and `pyrightconfig.json`
  - Fix logger type issues with `python scripts/add_type_hints.py`

- **Code Quality**:
  - Fully typed codebase with type annotations
  - Pre-commit hooks available: `poetry run pre-commit install`
  - Automated formatting with Ruff
