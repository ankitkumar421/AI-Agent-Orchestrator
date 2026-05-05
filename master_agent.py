import os
import sys
import streamlit as st

# --- 1. THE DDGS SHIM ---
# This fixes the "ModuleNotFoundError: No module named 'ddgs'" seen in image_0e3ce2.png
try:
    import duckduckgo_search
    sys.modules["ddgs"] = duckduckgo_search
except ImportError:
    pass

from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import create_sql_agent
from langchain_ollama import OllamaLLM
from langchain_community.tools import DuckDuckGoSearchRun
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, StorageContext, load_index_from_storage
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

# --- 2. CONFIGURATION ---
# Use the service name defined in docker-compose.yml
OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://ollama-service:11434")

# Initialize LLMs
# LangChain version for SQL/Search
llm_langchain = OllamaLLM(model="llama3", base_url=OLLAMA_HOST)
# LlamaIndex version for RAG (Knowledge Base)
llm_llamaindex = Ollama(model="llama3", base_url=OLLAMA_HOST, request_timeout=120.0)
embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")

# --- 3. TOOL INITIALIZATION ---
# SQL Tool
db = SQLDatabase.from_uri("sqlite:///sales.db")
search_tool = DuckDuckGoSearchRun()

# Knowledge Base (RAG) Logic
def get_kb_engine():
    if not os.path.exists("./storage"):
        # Load the "2026 growth strategy" document
        documents = SimpleDirectoryReader("./data").load_data()
        index = VectorStoreIndex.from_documents(documents, embed_model=embed_model)
        index.storage_context.persist()
    else:
        storage_context = StorageContext.from_defaults(persist_dir="./storage")
        index = load_index_from_storage(storage_context, embed_model=embed_model)
    return index.as_query_engine(llm=llm_llamaindex)

kb_engine = get_kb_engine()

# --- 4. MASTER AGENT LOGIC ---
def run_agent(user_prompt, chat_history=None):
    """
    Orchestrates between SQL, RAG, and Search to answer 
    complex Data Engineering & Strategy questions.
    """
    try:
        # Step 1: Check Internal Strategy (RAG)
        strategy_context = str(kb_engine.query(f"What does the 2026 strategy say about: {user_prompt}"))
        
        # Step 2: Check Sales Data (SQL)
        # We pass the prompt to a specialized SQL agent
        sql_agent = create_sql_agent(llm_langchain, db=db, verbose=False)
        sales_context = sql_agent.run(f"Query the database for: {user_prompt}")
        
        # Step 3: Check Market Trends (Search)
        market_context = search_tool.run(f"Current 2026 market trends in Pune for: {user_prompt}")

        # Final Synthesis
        final_prompt = f"""
        You are a Senior Data Strategist. Synthesize a report based on these 3 sources:
        1. Internal 2026 Strategy: {strategy_context}
        2. Actual Sales Data: {sales_context}
        3. Pune Market Trends: {market_context}
        
        User Question: {user_prompt}
        """
        
        return llm_langchain.invoke(final_prompt)
    
    except Exception as e:
        return f"Error in orchestration: {str(e)}"