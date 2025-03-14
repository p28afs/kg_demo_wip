from web import search  # OpenAI web search tool

def web_search(query):
    result = search(query)
    return result


import openai

def web_search(query):
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": query}],
        tools=[{"type": "web_search"}]  # Enabling web search
    )
    return response["choices"][0]["message"]["content"]

query = "Latest advancements in AI?"
print(web_search(query))




from langchain.vectorstores.neo4j_vector import Neo4jVector
from langchain.embeddings import OpenAIEmbeddings

# Load stored embeddings from Neo4j
vector_store = Neo4jVector.from_existing_graph(
    embedding=OpenAIEmbeddings(),
    url="bolt://localhost:7687",
    username="neo4j",
    password="password",
    node_label="Chunk",
    text_node_properties=["text"],
    embedding_node_property="embedding",
    index_name="shared_vector_index",
    keyword_index_name="shared_keyword_index",
    search_type="hybrid"
)

def rag_search(query):
    results = vector_store.similarity_search(query, k=5)
    return "\n".join([r.page_content for r in results])



def graph_rag_search(query):
    cypher_query = """
    CALL db.index.fulltext.queryNodes("entity_search", $query) YIELD node, score
    MATCH (node)<-[:MENTION]-(chunk:Chunk)
    RETURN chunk.text ORDER BY score DESC LIMIT 5
    """
    
    # Execute Cypher query in Neo4j
    with driver.session() as session:
        results = session.run(cypher_query, query=query)
        return "\n".join([record["chunk.text"] for record in results])



from langchain.chat_models import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o", temperature=0)

def compare_answers(query):
    web_answer = web_search(query)
    rag_answer = rag_search(query)
    graph_rag_answer = graph_rag_search(query)

    # Create a comparison prompt
    comparison_prompt = f"""
    Compare the following three answers to the query: "{query}".

    1️⃣ Web Search Answer (real-time data):
    {web_answer}

    2️⃣ RAG Answer (Vector Search):
    {rag_answer}

    3️⃣ Graph RAG Answer (Entity-Aware Retrieval):
    {graph_rag_answer}

    - Identify key differences.
    - Evaluate which source provides the **most reliable, accurate, and complete answer**.
    - Explain if **combining** these approaches would improve accuracy.

    Provide a **clear, structured evaluation**.
    """

    response = llm.predict(comparison_prompt)
    return response

# Example Query
query = "What are the latest advancements in AI?"
evaluation = compare_answers(query)
print(evaluation)

