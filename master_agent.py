import re
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.utilities import SQLDatabase
from langchain_core.output_parsers import StrOutputParser
from ddgs import DDGS

# 1. INITIALIZATION: Setup DB and local Llama 3
db = SQLDatabase.from_uri("sqlite:///sales.db")
schema = db.get_table_info()
llm = ChatOllama(model="llama3", temperature=0)

# --- TOOL 1: HARDENED INTERNET SEARCH ---
def search_internet(user_question):
    refine_prompt = ChatPromptTemplate.from_template(
        "SYSTEM: You are a search query optimizer. Output ONLY the search query string. \n"
        "No explanations. No conversational text. \n"
        "USER: Convert this into a business news search: {question}"
    )
    raw_query = (refine_prompt | llm | StrOutputParser()).invoke({"question": user_question})
    clean_query = raw_query.split('\n')[0].replace("`", "").strip()
    
    with DDGS() as ddgs:
        print(f"-> Sending Optimized Query: {clean_query}")
        try:
            results = list(ddgs.text(clean_query, max_results=3))
            if not results: return "No real-time data found."
            return "\n\n".join([f"Source: {r['title']}\nContent: {r['body']}" for r in results])
        except Exception as e:
            return f"Search failed: {e}"

# --- TOOL 2: SQL LOGIC WITH TAG EXTRACTION & HITL ---
def run_sql_with_hitl(question, initial_sql, attempts=3):
    current_query = initial_sql
    for i in range(attempts):
        # Clean: Look for <SQL> tags first, fallback to regex-based cleaning
        match = re.search(r'<SQL>(.*?)</SQL>', current_query, re.DOTALL | re.IGNORECASE)
        clean_query = match.group(1).strip() if match else current_query.replace("```sql", "").replace("```", "").split(';')[0].strip() + ";"
        
        print(f"\n--- [AGENT PROPOSAL] ---")
        print(f"I intend to run this SQL: {clean_query}")
        choice = input("Approve? (y/n/f): ").lower()
        
        if choice == 'n': return None, "Operation cancelled."
        if choice == 'f': clean_query = input("Enter corrected SQL: ")

        try:
            print(f"-> Executing SQL...")
            result = db.run(clean_query)
            return clean_query, result
        except Exception as e:
            print(f"-> Error: {e}")
            if i == attempts - 1: return None, "Max retries reached."
            fix_p = ChatPromptTemplate.from_template("SQL {query} failed: {error}. Rewrite between <SQL/> tags.")
            current_query = (fix_p | llm | StrOutputParser()).invoke({"query": clean_query, "error": str(e)})

# --- 2. CHAIN DEFINITIONS (Defined BEFORE the master agent) ---

# A. The "Brain": Task Decomposition
decomp_prompt = ChatPromptTemplate.from_template(
    "SYSTEM: You are a precision router. Output ONLY the tasks in the exact format: \n"
    "SQL: [query_task] | SEARCH: [search_task] \n"
    "Do not include introductory text or bullet points.\n"
    "QUESTION: {question}"
)
decomp_chain = decomp_prompt | llm | StrOutputParser()

# B. The SQL Generator
sql_p = ChatPromptTemplate.from_template(
    "Write SQL between <SQL> and </SQL> tags. Table: daily_sales. Schema: {schema}\n"
    "USER: {question}"
)
sql_chain = sql_p | llm | StrOutputParser()

# C. The Synthesis (The "ans_chain" you needed!)
ans_prompt = ChatPromptTemplate.from_template(
    "SYSTEM: You are a Senior Data Analyst. Your goal is to be BRIEF and DATA-DRIVEN. \n"
    "RULES:\n"
    "1. Use a Markdown Table for all raw data comparison.\n"
    "2. FORMATTING: All revenue and price figures MUST include the '₹' symbol (e.g., ₹25,000.00).\n"
    "3. ACCURACY: Use the exact numbers provided in the 'DATA GATHERED' section.\n"
    "4. Maximum 3 bullet points for 'Executive Insights'.\n"
    "\n"
    "USER QUESTION: {question}\n"
    "DATA GATHERED: {result}\n"
    "REPORT:"
)
ans_chain = ans_prompt | llm | StrOutputParser()

# --- 3. MASTER ORCHESTRATOR ---
def run_master_agent(question):
    print(f"\n[REQUEST]: {question}")
    
    # Step 1: Decompose
    decomposition = decomp_chain.invoke({"question": question})
    print(f"[DECOMPOSITION]: {decomposition}")

    sql_task = decomposition.split("SQL:")[1].split("|")[0].strip() if "SQL:" in decomposition else ""
    search_task = decomposition.split("SEARCH:")[1].strip() if "SEARCH:" in decomposition else ""

    internal_data = "No internal data needed."
    external_data = "No external data needed."

    # Step 2: Execute SQL
    if sql_task and len(sql_task) > 5:
        initial_sql = sql_chain.invoke({"schema": schema, "question": sql_task})
        _, internal_data = run_sql_with_hitl(sql_task, initial_sql)

    # Step 3: Execute Search
    if search_task and len(search_task) > 5:
        external_data = search_internet(search_task)

    # Step 4: Final Synthesis
    print("-> Merging all sources for final report...")
    return ans_chain.invoke({
        "question": question, 
        "result": f"INTERNAL SQL: {internal_data}\nEXTERNAL NEWS: {external_data}"
    })

if __name__ == "__main__":
    test_q = "We sold a lot of 'Soft Drinks' in Pune-Hinjewadi recently. Does the current weather forecast for Pune suggest this trend will continue or should we manage inventory for rain?"
    print(run_master_agent(test_q))