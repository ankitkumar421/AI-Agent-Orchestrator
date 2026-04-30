# 🤖 Autonomous AI Data Analyst Orchestrator



> **Bridging Structured Sales Data and Real-time Market Intelligence**

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![LangChain](https://img.shields.io/badge/Framework-LangChain-green?style=for-the-badge&logo=langchain)](https://www.langchain.com/)
[![Ollama](https://img.shields.io/badge/Inference-Local%20Ollama-orange?style=for-the-badge&logo=docker)](https://ollama.ai/)
[![SQLite](https://img.shields.io/badge/Database-SQLite-lightblue?style=for-the-badge&logo=sqlite)](https://www.sqlite.org/)
[![Streamlit](https://img.shields.io/badge/UI-Streamlit-red?style=for-the-badge&logo=streamlit)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active%20Development-blue?style=for-the-badge)](https://github.com/ankitkumar421/AI-Agent-Orchestrator)

---

## 📋 Table of Contents

- [Overview](#-project-overview)
- [Key Features](#-key-features)
- [Architecture](#-system-architecture)
- [Installation](#-installation--setup)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [Roadmap](#-roadmap--evolution)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🎯 Project Overview

This project features an advanced **Multi-Agent Orchestrator** designed for modern business intelligence. It goes beyond simple chatbots—it **reasons**, **decomposes** complex queries, and **synthesizes** insights from both internal databases and real-time market data.

### 🚀 Key Capabilities

- **🧠 Intelligent Task Decomposition**: Breaks down complex business questions into precise SQL queries and market research tasks
- **🛡️ Self-Healing SQL**: Reflection loop that identifies syntax errors and auto-corrects queries before execution
- **🤝 Human-in-the-Loop (HITL)**: Dedicated security gate for manual SQL query verification before execution
- **🌍 Real-time Market Context**: Live search integration (DuckDuckGo API) for market trends and business intelligence
- **📊 Executive Reporting**: Automatic formatting into professional tables with INR (₹) currency formatting
- **🔍 Multi-Source Intelligence**: Seamlessly combines internal sales data with external market insights

---

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                     USER QUESTION                                │
└────────────────────────┬────────────────────────────────────────┘
                         │
        ┌────────────────▼──────────────────┐
        │   MASTER ORCHESTRATOR (Llama 3)   │
        │   • Task Decomposition            │
        │   • Response Synthesis            │
        └────────────┬───────────┬──────────┘
                     │           │
         ┌───────────▼──┐    ┌───▼───────────┐
         │  SQL AGENT   │    │ SEARCH AGENT  │
         └───────┬──────┘    └───┬───────────┘
                 │               │
        ┌────────▼────────┐  ┌───▼──────────────┐
        │  SQLite (sales) │  │ DuckDuckGo API   │
        │  • daily_sales  │  │ • Market Trends  │
        │  • price data   │  │ • News & Context │
        └─────────────────┘  └──────────────────┘
                 │               │
        ┌────────▼───────────────▼────────┐
        │   DATA SYNTHESIS & FORMATTING   │
        │   (Executive Report with INR)   │
        └───────────────┬──────────────────┘
                        │
        ┌───────────────▼──────────────────┐
        │  STREAMLIT DASHBOARD (Frontend)  │
        │  • Interactive UI                │
        │  • Real-time Visualization       │
        └────────────────────────────────────┘
```

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **Reasoning Engine** | Llama 3 (8B) via Ollama | Query decomposition, synthesis, and reasoning |
| **Orchestration** | LangChain (LCEL) | Agent flow management and tool coordination |
| **Data Storage** | SQLite | Lightweight, local sales data repository |
| **Search Integration** | DuckDuckGo API | Real-time market intelligence & trends |
| **User Interface** | Streamlit | Interactive, reactive dashboard for end-users |
| **Task Queue** | Native Python | Async task execution and error handling |

---

## 🛠️ Installation & Setup

### Prerequisites

- **Python 3.10+**
- **Ollama** (for local Llama 3 inference) - [Download here](https://ollama.ai/)
- **SQLite** (usually pre-installed)
- **pip** (Python package manager)

### Step 1: Clone the Repository

```bash
git clone https://github.com/ankitkumar421/AI-Agent-Orchestrator.git
cd AI-Agent-Orchestrator
```

### Step 2: Set Up Python Virtual Environment

```bash
# Create virtual environment
python -m venv ai_env

# Activate it
# On Windows:
ai_env\Scripts\activate

# On macOS/Linux:
source ai_env/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

**Key dependencies:**
- `langchain`
- `langchain-ollama`
- `langchain-community`
- `streamlit`
- `duckduckgo-search`
- `sqlite3`

### Step 4: Initialize the Database

```bash
python create_database.py
```

This creates the `sales.db` SQLite database with sample sales records.

### Step 5: Start Ollama (Local LLM Server)

```bash
ollama serve
```

In another terminal, pull the Llama 3 model:

```bash
ollama pull llama3
```

### Step 6: Launch the Streamlit Dashboard

```bash
streamlit run app.py
```

The dashboard will open at `http://localhost:8501`

---

## 💡 Usage


https://github.com/user-attachments/assets/1cb06df5-eeee-432f-ba2a-e1768a0497ad


### 1. **Ask a Business Question**

Enter a natural language query like:
- _"Compare our Pune revenue to national burger price trends"_
- _"What products are trending in Hinjewadi?"_
- _"How does our Soft Drinks sales correlate with weather patterns?"_

### 2. **Agent Decomposition**

The Master Agent automatically breaks down your question into:
- **SQL Task**: Query internal sales database
- **Search Task**: Fetch real-time market data

### 3. **Human Approval (HITL)**

Before execution, proposed SQL queries are presented for verification:
```
[AGENT PROPOSAL]
I intend to run this SQL: SELECT * FROM daily_sales WHERE region = 'Pune'
Approve? (y/n/f):
```
- **y** = Execute
- **n** = Cancel
- **f** = Modify and resubmit

### 4. **Get Executive Reports**

Receive formatted reports with:
- **Markdown tables** for data comparison
- **INR currency formatting** (₹25,000.00)
- **Market insights** from web search
- **Trend analysis** and recommendations

---

## 📁 Project Structure

```
AI-Agent-Orchestrator/
├── app.py                      # Streamlit dashboard UI
├── master_agent.py             # Core orchestrator & agent logic
├── sql_bridge.py               # SQL query execution & error handling
├── create_database.py          # Database initialization script
├── test_search.py              # Search integration tests
├── requirements.txt            # Python dependencies
├── sales.db                    # SQLite database (generated)
├── .gitignore                  # Git ignore rules
└── README.md                   # This file
```

### File Descriptions

| File | Purpose |
|------|---------|
| `app.py` | Streamlit frontend with UI components, status indicators, and data exploration |
| `master_agent.py` | Main orchestrator—decomposes queries, manages SQL/search agents, synthesizes reports |
| `sql_bridge.py` | Handles SQL query execution, error correction, and HITL verification |
| `create_database.py` | Populates SQLite with sample sales data (regions, products, dates, revenue) |
| `test_search.py` | Unit tests for DuckDuckGo search integration |

---

## 📸 Dashboard Preview

### Example Query:
> _"What is the revenue for Classic Burgers in Pune-Hinjewadi compared to the national average?"_

### Generated Report:

| Metric | Value |
|--------|-------|
| **Internal Sales (Pune)** | **₹45,200.00** |
| **Market Avg Price** | **₹185.00** |
| **Trend Analysis** | **Outperforming by 15%** ✅ |
| **Recommendation** | Scale inventory for summer season |

---

## 🚀 Advanced Features

### Self-Healing SQL

If a query fails, the agent automatically attempts fixes:

```python
# Example
Initial Query: SELECT * FROM sales WHERE date = '2024-01-01'  # ❌ Column doesn't exist
Agent Fix:    SELECT * FROM daily_sales WHERE sale_date = '2024-01-01'  # ✅
```

### Task Decomposition

Complex questions are split into parallel tasks:

```
USER: "Compare regional sales trends with weather patterns"

DECOMPOSITION:
├── SQL Task: "Get Q1 sales by region"
└── Search Task: "Q1 2024 weather patterns by region"

EXECUTION: Parallel execution → Merged synthesis → Report
```

### HITL Security

Every SQL operation requires human approval before execution, preventing:
- Unintended data deletions
- Sensitive information exposure
- Database corruption

---

## 📅 Roadmap & Evolution

- [x] **Phase 1**: SQL & Search Integration ✅
- [x] **Phase 2**: Streamlit UI & HITL Security ✅
- [ ] **Phase 3**: LlamaIndex RAG for internal PDF policy analysis
- [ ] **Phase 4**: Migration to AWS CloudWatch for agent monitoring
- [ ] **Phase 5**: Multi-LLM support (GPT-4, Claude, Gemini)
- [ ] **Phase 6**: Advanced visualization with Plotly/Dash

---

## 🤝 Contributing

We welcome contributions! Whether you want to:
- Add new tools or agents
- Optimize prompts and decomposition logic
- Improve the UI
- Fix bugs or enhance performance

Please feel free to:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/awesome-feature`)
3. Commit your changes (`git commit -m 'Add awesome feature'`)
4. Push to the branch (`git push origin feature/awesome-feature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 🙋 Support & Questions

Have questions or encountered issues? 

- 📧 Open an [Issue](https://github.com/ankitkumar421/AI-Agent-Orchestrator/issues)
- 💬 Start a [Discussion](https://github.com/ankitkumar421/AI-Agent-Orchestrator/discussions)
- 🐛 Report a [Bug](https://github.com/ankitkumar421/AI-Agent-Orchestrator/issues/new?labels=bug)

---

## 🌟 Acknowledgments

- **LangChain** for the powerful orchestration framework
- **Meta** for Llama 3 model
- **Ollama** for local LLM inference
- **Streamlit** for the amazing dashboard framework
- **DuckDuckGo** for privacy-respecting search API

---

**Made with ❤️ by [ankitkumar421](https://github.com/ankitkumar421)**

*Star ⭐ this repo if you found it helpful!*
