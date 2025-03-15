from langchain.embeddings import OpenAIEmbeddings

# Initialize embedding model
embedding_model = OpenAIEmbeddings(model="text-embedding-ada-002")

# Generate embeddings and store them in Neo4j
for doc in graph_documents:
    embedding = embedding_model.embed_query(doc.text)  # Generate embedding

    # Store embedding in Neo4j
    graph.query(
        """
        MERGE (d:Document {id: $id})
        SET d.text = $text,
            d.embedding = $embedding
        RETURN d
        """,
        params={"id": doc.id, "text": doc.text, "embedding": embedding}
    )

print("✅ Embeddings stored in Neo4j")
