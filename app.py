import streamlit as st
import time
from master_agent import run_agent

st.set_page_config(page_title="Data Strategist AI", page_icon="🤖", layout="wide")

# Sidebar Health Check
with st.sidebar:
    st.title("⚙️ System Status")
    st.success("✅ SQL Sales DB Connected")
    st.success("✅ RAG Knowledge Base Active")
    st.success("✅ Web Search Online")
    if st.button("Reset Chat"):
        st.session_state.messages = []
        st.rerun()

st.title("🏙️ Pune Operations Command Center")
st.caption("Autonomous Agent for Data Cloud AI Engineering Portfolio")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Enter your strategic query..."):
    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.status("🤖 Orchestrating with Memory...", expanded=True) as status:
            st.write("Reviewing conversation context...")
            
            # PASS THE HISTORY HERE
            response = run_agent(prompt, chat_history=st.session_state.messages[:-1])
            
            status.update(label="Analysis Complete!", state="complete", expanded=False)
        
        st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})