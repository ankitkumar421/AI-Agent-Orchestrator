# 🤖 Autonomous AI Data Analyst Orchestrator

> **Bridging Structured Sales Data & Real-time Market Intelligence**  

A production-grade agentic RAG system designed to automate complex business intelligence tasks through intelligent orchestration of SQL databases, retrieval-augmented generation, and live market data.

## 📊 Status & Badges

[![Python](https://img.shields.io/badge/Python-3.12%2B-3776ab?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![LangChain](https://img.shields.io/badge/LangChain-Framework-00d084?style=flat-square&logo=langchain&logoColor=white)](https://www.langchain.com/)
[![Llama3](https://img.shields.io/badge/Llama3-8B%20Model-FF6B00?style=flat-square&logo=meta&logoColor=white)](https://llama.meta.com/)
[![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?style=flat-square&logo=docker&logoColor=white)](https://www.docker.com/)
[![SQLite](https://img.shields.io/badge/SQLite-Lightweight%20DB-003B57?style=flat-square&logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-UI-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square)](https://github.com/ankitkumar421/AI-Agent-Orchestrator)

---

## 📑 Quick Navigation

- [✨ Features](#-key-features)
- [🏗️ Architecture](#-system-architecture)  
- [🚀 Getting Started](#-quick-start)
- [💡 Real-World Examples](#-real-world-use-case)
- [📁 Project Structure](#-project-structure)
- [🛣️ Roadmap](#-roadmap--evolution)
- [🤝 Contributing](#-contributing)

---

## 🎯 Project Overview

This is an **enterprise-grade Multi-Agent Orchestrator** built for the modern data strategist. Unlike simple LLM chatbots, this system:

- 🧠 **Reasons** over your unique business context
- 🔄 **Decomposes** complex queries into actionable data tasks
- 🔗 **Synthesizes** insights from multiple data sources
- ✅ **Verifies** decisions through human-in-the-loop gates
- 📊 **Reports** in professional, formatted outputs

### Perfect For:
- 📈 Data strategists analyzing regional performance
- 🏢 Business analysts bridging SQL and market trends
- 🛍️ Retail managers making competitive pricing decisions
- 📊 Executive teams requiring data-driven synthesis

---

## ✨ Key Features

| Feature | Description | Benefit |
|---------|-------------|---------|
| 🧠 **Smart Decomposition** | Breaks complex questions into SQL + search tasks | Faster, more accurate answers |
| 🛡️ **Self-Healing SQL** | Auto-detects & corrects query syntax errors | Fewer failed queries |
| 🤝 **Human-in-the-Loop** | Manual approval gate before data operations | Enterprise security |
| 🌍 **Real-Time Market Data** | Live DuckDuckGo integration | Always current intelligence |
| 💰 **INR Currency Formatting** | Automatic ₹ formatting for reports | Professional Indian market reporting |
| 📊 **Executive Reports** | Markdown tables with trend analysis | Boardroom-ready insights |
| 🔍 **Multi-Source Intelligence** | Merges internal sales + external trends | Complete business picture |
| 🐳 **Fully Dockerized** | Complete containerized stack | Deploy anywhere, no setup hassles |

---

## 🏗️ System Architecture

```
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                    🌐 USER QUESTION                          ┃
┃               (Natural Language Query)                        ┃
┗━━━━━━━━━━━━━━━━━━━━━━━┬━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
                       │
       ┏━━━━━━━━━━━━━━━▼━━━━━━━━━━━━━━━┓
       ┃  🤖 MASTER ORCHESTRATOR       ┃
       ┃    (Llama 3 8B Reasoning)     ┃
       ┃  • Query Decomposition        ┃
       ┃  • Task Planning              ┃
       ┃  • Response Synthesis         ┃
       ┗━━━━━━┬──────────────────┬─────┛
              │                  │
     ┌────────▼────────┐  ┌──────▼──────────┐
     ┃  📊 SQL AGENT   ┃  ┃  🔍 SEARCH AGENT┃
     └────────┬────────┘  └──────┬──────────┘
              │                  │
     ┌────────▼───────────┐  ┌───▼───────────┐
     ┃  💾 SQLite DB      ┃  ┃ 🌐 DuckDuckGo ┃
     ┃  • sales.db        ┃  ┃  • Live Data  ┃
     ┃  • Price Index     ┃  ┃  • Trends     ┃
     ┃  • Regional Data   ┃  ┃  • Market News┃
     ┗────────┬───────────┘  ┗───┬───────────┘
              │                  │
       ┌──────▼──────────────────▼────────┐
       ┃  📈 SYNTHESIS & FORMATTING       ┃
       ┃  • Data Merging                  ┃
       ┃  • Trend Analysis                ┃
       ┃  • Report Generation             ┃
       ┗──────┬──────────────────────────┘
              │
       ┌──────▼──────────────────────────┐
       ┃  ✅ HUMAN REVIEW GATE (HITL)    ┃
       ┃  • SQL Verification             ┃
       ┃  • Approval/Rejection           ┃
       ┗──────┬──────────────────────────┘
              │
       ┌──────▼──────────────────────────┐
       ┃  📊 STREAMLIT DASHBOARD         ┃
       ┃  • Interactive UI               ┃
       ┃  • Real-time Results            ┃
       ┃  • Data Exploration             ┃
       ┗──────────────────────────────────┘
```

### 🔧 Technology Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **🧠 Reasoning** | Llama 3 (8B) via Ollama | Complex query decomposition & synthesis |
| **🎯 Orchestration** | LangChain (LCEL) | Seamless agent flow management |
| **💾 Data Storage** | SQLite | Fast, local sales database |
| **🔍 Search** | DuckDuckGo API | Privacy-respecting market intelligence |
| **🎨 Interface** | Streamlit | Reactive, interactive dashboard |
| **🐳 Containerization** | Docker Compose | Multi-container orchestration |
| **📦 Python** | 3.12-slim | Modern, stable runtime |

---

## 🚀 Quick Start

### Prerequisites
- 🐳 Docker Desktop (latest)
- 📝 Git
- 💾 2GB free disk space

### Installation

```bash
# 1️⃣ Clone Repository
git clone https://github.com/ankitkumar421/AI-Agent-Orchestrator.git
cd AI-Agent-Orchestrator

# 2️⃣ Launch Everything with Docker Compose
docker-compose up --build

# 3️⃣ Pull Llama 3 Model (in another terminal)
docker exec -it ai_agent_project-ollama-service-1 ollama run llama3

# 4️⃣ Open Dashboard
# Navigate to: http://localhost:8501
```

That's it! The entire stack is now running.

---

## 💡 Real-World Use Case

Compare our Hinjewadi Classic Burger revenue against 2026 growth targets. Are we priced competitively vs. the Pune market?

What Happens Behind the Scenes: Decomposition into SQL and search tasks, parallel execution, data synthesis, and professional report generation with INR formatting.

---

## 📁 Project Structure

```
AI-Agent-Orchestrator/
├── docker-compose.yml          # Multi-container orchestration
├── Dockerfile                  # Python 3.12-slim image
├── master_agent.py             # Core orchestrator & reasoning
├── app.py                      # Streamlit dashboard
├── sql_bridge.py               # SQL execution & HITL gate
├── create_database.py          # DB initialization
├── requirements.txt            # Python dependencies
├── sales.db                    # SQLite database
└── README.md                   # This file
```

---

## 🛣️ Roadmap & Evolution

### ✅ Completed
- [x] SQL + Search integration
- [x] Streamlit dashboard
- [x] Human-in-the-loop verification
- [x] Docker containerization

### 🚧 In Progress
- [ ] LlamaIndex RAG for internal PDFs
- [ ] AWS CloudWatch monitoring
- [ ] Advanced visualization

### 🔮 Future
- [ ] Multi-LLM support (GPT-4, Claude)
- [ ] Graph database integration
- [ ] Mobile app companion

---

## 🤝 Contributing

Fork → Feature Branch → Commit → Push → Pull Request

---

## 📝 License

MIT License - see [LICENSE](LICENSE) for details.

---

## 🆘 Support

- 📧 [Open an Issue](https://github.com/ankitkumar421/AI-Agent-Orchestrator/issues)
- 💬 [Start a Discussion](https://github.com/ankitkumar421/AI-Agent-Orchestrator/discussions)
- 🐛 [Report a Bug](https://github.com/ankitkumar421/AI-Agent-Orchestrator/issues/new?labels=bug)

---

Made with ❤️ by [ankitkumar421](https://github.com/ankitkumar421)

Star ⭐ this repo if you found it helpful!