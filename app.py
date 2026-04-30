import streamlit as st
import time
from master_agent import run_master_agent, db # Importing your core logic

# --- UI CONFIGURATION ---
st.set_page_config(
    page_title="Autonomous AI Data Analyst",
    page_icon="📊",
    layout="wide"
)

# Custom CSS for a professional look
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stTextInput > div > div > input { background-color: #ffffff; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR: SYSTEM OBSERVABILITY ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2103/2103633.png", width=80)
    st.title("Agent Control Center")
    st.markdown("---")
    st.info("**Model:** Llama 3 (8B) via Ollama")
    st.info("**Environment:** Local Inference")
    st.success("**Database:** Connected (sales.db) ✅")
    st.success("**Internet Search:** Enabled (DDGS) ✅")
    st.markdown("---")
    if st.button("Clear History"):
        st.rerun()

# --- MAIN INTERFACE ---
st.title("🤖 Autonomous AI Data Analyst")
st.caption("Bridging Internal SQL Data and Real-time Market Intelligence")

# 1. User Input
user_query = st.text_input(
    "Enter your business question:",
    placeholder="e.g., 'Compare our Pune revenue to national burger price trends'"
)

# 2. Execution & Display
if user_query:
    # Use a container to show progress
    with st.status("Agent is working...", expanded=True) as status:
        st.write("🔍 Decomposing query into tasks...")
        time.sleep(1) # Simulation for visual effect
        
        # Call your Master Agent
        # Note: We temporarily remove the HITL 'input()' for the UI version 
        # or handle it via Streamlit buttons (advanced).
        try:
            report = run_master_agent(user_query)
            status.update(label="Analysis Complete!", state="complete", expanded=False)
            
            # 3. Present the Final Report
            st.markdown("---")
            st.subheader("📋 Executive Business Report")
            st.markdown(report)
            
        except Exception as e:
            st.error(f"Execution Error: {e}")

# --- DATA EXPLORATION TAB ---
st.markdown("---")
with st.expander("📂 Raw Data Explorer"):
    st.write("Showing recent records from `daily_sales`:")
    raw_data = db.run("SELECT * FROM daily_sales LIMIT 5")
    st.code(raw_data, language="sql")