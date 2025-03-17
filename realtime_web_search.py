from langchain.chat_models import ChatOpenAI
from langchain.tools import Tool
from langchain.agents import initialize_agent
from langchain.schema import SystemMessage

# Define a web search tool (replace with an actual API call)
def web_search(query):
    return f"Performing a web search for: {query}"  # Replace with real API call

# Wrap the function as a LangChain tool
search_tool = Tool(
    name="Web Search",
    func=web_search,
    description="Searches the web for real-time information."
)

# Initialize the OpenAI model with function calling
llm = ChatOpenAI(model="gpt-4-turbo", temperature=0)

# Create an agent with the web search tool
agent = initialize_agent(
    tools=[search_tool],
    llm=llm,
    agent="zero-shot-react-description",
    verbose=True
)

# Use ainvoke to fetch real-time data
async def run_query():
    response = await agent.ainvoke("Find the latest news about AI.")
    print(response)

# Call the async function
import asyncio
asyncio.run(run_query())
