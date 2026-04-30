from duckduckgo_search import DDGS

# This script mimics a "Search Tool" for an AI agent
def search_internet(query):
    with DDGS() as ddgs:
        print(f"Searching for: {query}...")
        results = ddgs.text(query, max_results=3)
        return results

# Let's test it with a real-time query
try:
    search_results = search_internet("Current weather in Pune")
    
    for i, result in enumerate(search_results, 1):
        print(f"\nResult {i}:")
        print(f"Title: {result['title']}")
        print(f"Snippet: {result['body']}")
        print(f"Link: {result['href']}")
except Exception as e:
    print(f"An error occurred: {e}")