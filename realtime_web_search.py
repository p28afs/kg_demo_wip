import asyncio
import langchain
from langchain.chat_models import ChatOpenAI
from langchain.tools import Tool
from langchain.agents import initialize_agent
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from langchain.schema import SystemMessage

# Enable debugging to see full LLM responses
langchain.debug = True

# Define a web search tool (Mock function; replace with real API)
def web_search(query):
    return f"Performing a web search for: {query}"  # Replace with actual web search API

# Wrap the function as a LangChain tool
search_tool = Tool(
    name="Web Search",
    func=web_search,
    description="Searches the web for real-time information."
)

# Define expected output format
response_schemas = [
    ResponseSchema(name="search_results", description="List of search results related to PTRR ID."),
    ResponseSchema(name="error", description="Error details if any.")
]

output_parser = StructuredOutputParser.from_response_schemas(response_schemas)
format_instructions = output_parser.get_format_instructions()

# Initialize OpenAI Chat Model
llm = ChatOpenAI(model="gpt-4-turbo", temperature=0)

# Create an agent with the web search tool
agent = initialize_agent(
    tools=[search_tool],
    llm=llm,
    agent="zero-shot-react-description",
    verbose=True
)

# Async function to perform web search and parse output
async def run_query():
    try:
        # Prompt LLM with structured output instructions
        query = f"Perform a web search for 'PTRR ID details format validations'. {format_instructions}"
        llm_response = await llm.ainvoke(query)

        # Parse LLM response
        parsed_output = output_parser.parse(llm_response)
        print("Parsed Output:", parsed_output)

    except Exception as e:
        print("Error occurred:", str(e))
        print("Raw LLM Response:", llm_response)

# Run the async function
asyncio.run(run_query())
