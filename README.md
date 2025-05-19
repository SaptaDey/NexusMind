# 🧠 NexusMind

<div align="center">

<img src="https://raw.githubusercontent.com/SaptaDey/NexusMind/main/static/asr-got-logo.png" width="180" height="180" alt="NexusMind Logo"/>

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
  <img src="https://mermaid.ink/img/pako:eNp1k89OwzAMxl8l8nGyFwjXHUDiAKfdOCCOJnFH0WLXadIVofa92Z9Oy8YOiWx9v9j-7Oim5NwjyZW8RANWn4ypHSgqqgaDjRMH0mOXXI7EGKtbaCgL69LBEx0Ui_XeEXRxt9gWTbAkE8sMxivYruDRQe3RfQIxGD9FWNkLxKR5x2y4t7ZH-KpVNsYfQacxaxzHUEULmP6qfXpvkFS_dAohGQlGjyzOoJzO2JWxKloheyPGdZfMrWnejUFzw_m0jGv_jE3P5vhhTQf3yLmlVuUr0-mhxeCkOgeDsQM9VhZ7Tuk3IbIuH81x_tZwNfRzesf_yaMpEOuCiy6_l2OnEiTqnlVbedI-ObXuj4qafIkz_fjcJ8kJ5KR2atpa53WXVavWu--H77-WVJ9Sueb9eNLtYMrjRZzc9njFo4dLuz3oz4WnbLw4jQtns9lkuPlztXSh_3hUcGZzeg7EXpyDOLlycn7jpvRRnU_4uEKTiCYsfCIuut8F1AeySl2lGhQK6RtS2CKtpCmkVmBJyYGUe-39nZSIhtwdSuUIP9KrXKNG3tbS_2Zkc8I?type=png" width="700" height="350"/>
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
      <td align="center"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="38" height="38"/><br>Python 3.13+</td>
      <td align="center"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/fastapi/fastapi-original.svg" width="38" height="38"/><br>FastAPI</td>
      <td align="center"><img src="https://networkx.org/documentation/latest/_static/networkx_logo.svg" width="38" height="38"/><br>NetworkX</td>
      <td align="center"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/docker/docker-original.svg" width="38" height="38"/><br>Docker</td>
    </tr>
    <tr>
      <td align="center"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pytest/pytest-original.svg" width="38" height="38"/><br>Pytest</td>
      <td align="center"><img src="https://docs.pydantic.dev/latest/logo-white.svg" width="38" height="38"/><br>Pydantic</td>
      <td align="center"><img src="https://python-poetry.org/images/logo-origami.svg" width="38" height="38"/><br>Poetry</td>
      <td align="center"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/uvicorn/uvicorn-original.svg" width="38" height="38"/><br>Uvicorn</td>
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
   cd asr-got-reimagined
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
  <img src="https://mermaid.ink/img/pako:eNptkk1vwjAMhv9KlBNIaIhttzL1wGFjE9OQ9tFLE5eaJs6UuKAW8d9noCDKYS9-7OextfuKSs-RV-LsJX7j_nWBhoOSQLuSQkXvKtxNlu1s8HyKiZNiDre3OnJ1apItoxXa4K2Re0jecVeZOL01JsdN4tR9-njFHbke1xSj1cnZZIXG-mTfQfdJc_A87-nj4ajBKmrB3xPXumYXNla-9DPmQBox_OfRUkvW4ieuOtgGR7CzrptGfzRwW-dqdTN4nbH1Z5eNis36Z5JK9Rn6QLJDkdMTjYvMXBHDGoFcE-Yllc5IE3ddopDjPA-zeLHMwnSQpWy6mLOb-2UcxbNinI6mcTZih3Kc55Pw_i_wPK_APAuiMIzYoViGUTQdxDMWlSXbYyWGZAavWQ6VwbKkshHp84-0nUxUXxukbdzj93q5_wFAuLEJ?type=png" width="400" height="200"/>
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
