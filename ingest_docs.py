import os
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, StorageContext, load_index_from_storage, Settings
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

# 1. SETUP: Configure LlamaIndex to use local Llama 3 and Local Embeddings
# We use HuggingFace for embeddings because it's fast and runs entirely on your GPU/CPU
Settings.llm = Ollama(model="llama3", request_timeout=360.0)
Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")

PERSIST_DIR = "./storage"
DATA_DIR = "./data"

def create_or_load_index():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
        return None

    if not os.path.exists(PERSIST_DIR):
        print("🔍 DEBUG: Extracting text from files...")
        documents = SimpleDirectoryReader(DATA_DIR).load_data()
        
        # --- NEW DEBUG LINE ---
        for doc in documents:
            print(f"📄 File: {doc.metadata['file_name']}")
            print(f"📝 Content Snippet: {doc.text[:500]}...") # Print first 500 characters
        # ----------------------

        index = VectorStoreIndex.from_documents(documents)
        index.storage_context.persist(persist_dir=PERSIST_DIR)
    else:
        storage_context = StorageContext.from_defaults(persist_dir=PERSIST_DIR)
        index = load_index_from_storage(storage_context)
    
    return index

if __name__ == "__main__":
    index = create_or_load_index()
    if index:
        # Quick Test
        query_engine = index.as_query_engine()
        response = query_engine.query("What are the specific requirements for the beef used in the Classic Burger and what is the discount for IT employees?")
        print("\n--- [KNOWLEDGE BASE TEST] ---")
        print(response)