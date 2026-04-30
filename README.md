🤖 Autonomous AI Data Analyst Orchestrator

An advanced multi-agent system designed to bridge the gap between internal structured sales data and real-time external market intelligence. Built with LangChain, Ollama (Llama 3), and Streamlit, this orchestrator enables data-driven decision-making through natural language queries.



🌟 Core Features

Multi-Agent Task Decomposition: Utilizes LLM-based reasoning to break complex business questions into specific SQL (internal) and Search (external) sub-tasks.



Self-Healing SQL Engine: Features a reflection loop that autonomously identifies and fixes SQL syntax errors, ensuring high reliability for structured data retrieval.



Human-in-the-Loop (HITL) Security: Includes an approval gate that allows users to review and manually correct SQL queries before they touch the production database.



Real-time Market Context: Integrates with live web search APIs to fetch current news, competitor pricing, and economic trends (e.g., Pune-specific business insights).



Executive Dashboard: A production-ready Streamlit interface that presents findings in scannable Markdown tables with localized currency formatting (₹).



🛠️ Technical Stack

Logic \& Orchestration: LangChain (LCEL)



Inference Engine: Llama 3 (8B) running locally via Ollama



Internal Data: SQLite (Demonstrating expertise in SQL and Data Management)



External Intelligence: DuckDuckGo Search API



Application Layer: Streamlit (Python)



📂 Project Structure

Plaintext

├── app.py              # Streamlit Web Interface

├── master\_agent.py     # Core Orchestration, SQL, and Search Logic

├── sales.db            # SQLite Database (Sales Records)

├── create\_database.py  # Script to generate sample data

├── .gitignore          # Environment and database exclusion rules

└── requirements.txt    # Python dependencies

🚀 Getting Started

1\. Prerequisites

Python 3.10+



Ollama installed and running locally.



Llama 3 model pulled: ollama pull llama3



2\. Installation

Bash

\# Clone the repository

git clone https://github.com/ankitkumar421/AI-Agent-Orchestrator.git

cd AI-Agent-Orchestrator



\# Create and activate virtual environment

python -m venv ai\_env

source ai\_env/bin/scripts/activate  # On Windows: ai\_env\\Scripts\\activate



\# Install dependencies

pip install -r requirements.txt

3\. Usage

Run the dashboard to start interacting with the agent:



Bash

streamlit run app.py

📈 Future Roadmap

Document Intelligence (RAG): Integration of LlamaIndex to enable the agent to "read" and analyze internal company PDFs, strategy documents, and policy manuals.



Cloud Scaling: Migrating the database layer to AWS RDS/Redshift for enterprise-scale performance.



Multi-Modal Analysis: Adding the ability to interpret and generate charts and visual data summaries.



How to add this to your project:

In your terminal, type notepad README.md.



Paste the content above.



Save and close.



Run the final git update:



Bash

git add README.md

git commit -m "docs: add professional project documentation"

git push origin main

