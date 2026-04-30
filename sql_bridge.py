from langchain_community.chat_models import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.utilities import SQLDatabase
from langchain_core.output_parsers import StrOutputParser

# 1. Connect to Database
db = SQLDatabase.from_uri("sqlite:///sales.db")
schema = db.get_table_info()
llm = ChatOllama(model="llama3")

# 2. PROMPT: Generate SQL
sql_template = """Write ONLY the SQL query for this question based on the schema: {schema}
Question: {question}"""
sql_prompt = ChatPromptTemplate.from_template(sql_template)
sql_chain = sql_prompt | llm | StrOutputParser()

# 3. PROMPT: Interpretation (KPI Commentary)
ans_template = """The user asked: {question}
The SQL result was: {result}
Explain this result to the user in a professional, friendly way.But not in very long sentences. Just a concise commentary on the KPI."""
ans_prompt = ChatPromptTemplate.from_template(ans_template)
ans_chain = ans_prompt | llm | StrOutputParser()

# --- NEW: AGENTIC SELF-CORRECTION LOGIC ---
def run_query_with_self_correction(question, schema, initial_sql, attempts=2):
    current_query = initial_sql
    
    for i in range(attempts):
        try:
            # Clean and run the query
            clean_query = current_query.replace("```sql", "").replace("```", "").strip()
            print(f"\n[Attempt {i+1}] Running SQL: {clean_query}")
            result = db.run(clean_query)
            return clean_query, result # Success!
            
        except Exception as e:
            print(f"!!! Error detected: {e}")
            if i == attempts - 1:
                return None, f"Failed after {attempts} attempts. Error: {e}"
            
            # Reflection Step: AI fixes its own error
            print("AI is reflecting on the error and fixing the query...")
            fix_template = """The SQL query failed with this error: {error}
            Based on the schema: {schema}
            Rewrite the SQL query to fix the error. Output ONLY the SQL."""
            
            fix_prompt = ChatPromptTemplate.from_template(fix_template)
            fix_chain = fix_prompt | llm | StrOutputParser()
            
            current_query = fix_chain.invoke({"error": str(e), "schema": schema})

# --- RUNNING THE COMPLETE FLOW ---
user_question = "Show me the top 2 products by units sold in Mumbai-Andheri when no promotion was active."

# Step A: Get initial SQL
initial_sql = sql_chain.invoke({"schema": schema, "question": user_question})

# Step B: Run with Self-Correction loop
final_sql, raw_data = run_query_with_self_correction(user_question, schema, initial_sql)

if final_sql:
    # Step C: Get Final Answer (KPI Commentary)
    final_report = ans_chain.invoke({"question": user_question, "result": raw_data})
    print(f"\n--- BUSINESS REPORT ---")
    print(final_report)
else:
    print("\nAgent was unable to resolve the data issue.")