import openai
from duckduckgo_search import DDGS

# Set your OpenAI API key
OPENAI_API_KEY = "YOUR_OPENAI_API_KEY"
openai.api_key = OPENAI_API_KEY

# Function to search DuckDuckGo (No API key needed)
def duckduckgo_search(query, num_results=5):
    with DDGS() as ddgs:
        search_results = ddgs.text(query, max_results=num_results)

    snippets = []
    for result in search_results:
        title = result.get("title", "No Title")
        snippet = result.get("body", "No Description")
        url = result.get("href", "No URL")
        snippets.append(f"Title: {title}\nSnippet: {snippet}\nURL: {url}")
    
    return "\n\n".join(snippets)

# Function to ask GPT-4o using search results
def ask_gpt_with_search(query):
    # Get search results
    web_data = duckduckgo_search(query)
    
    # Format the prompt for GPT-4o
    prompt = f"""
    User Query: {query}

    Relevant Information from Web:
    {web_data}

    Please provide a well-structured and concise answer based on the above information.
    """
    
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are SearchGPT, an expert assistant that provides structured, up-to-date answers based on real-time web search results."},
            {"role": "user", "content": prompt}
        ]
    )
    
    return response["choices"][0]["message"]["content"]

# Example usage
if __name__ == "__main__":
    user_query = input("Enter your query: ")
    result = ask_gpt_with_search(user_query)
    print("\nSearchGPT Response:\n")
    print(result)
