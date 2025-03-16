import openai

# Set your OpenAI API key
openai.api_key = "YOUR_OPENAI_API_KEY"

# Function to query GPT-4o with web search
def ask_search_gpt(query):
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are SearchGPT, a professional assistant that provides structured and detailed answers using real-time web search."},
            {"role": "user", "content": query}
        ],
        tools=[{"type": "web_search"}],  # Enables real-time search
        tool_choice="web_search"  # Forces the model to use web search
    )
    
    # Extract the response
    return response["choices"][0]["message"]["content"]

# Example usage
if __name__ == "__main__":
    user_query = input("Enter your query: ")
    result = ask_search_gpt(user_query)
    print("\nSearchGPT Response:\n")
    print(result)
