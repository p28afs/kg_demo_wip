from neo4j import GraphDatabase

# Neo4j Connection Details
NEO4J_URI = "bolt://localhost:7687"  # Update with your Neo4j URI
NEO4J_USER = "neo4j"                 # Update with your username
NEO4J_PASSWORD = "password"          # Update with your password

# Index creation queries with IF NOT EXISTS check
INDEX_QUERIES = [
    """
    CALL db.indexes() YIELD name
    WITH collect(name) AS existingIndexes
    CALL apoc.do.when(
        "dgai_knowledge_text_index" IN existingIndexes,
        "",
        "CREATE FULLTEXT INDEX dgai_knowledge_text_index FOR (n:Document) ON EACH [n.text, n.category, n.document_type, n.legal_entities, n.publisher, n.regulator, n.regulatory_reporting_obligation];",
        {}
    ) YIELD value RETURN value;
    """,
    """
    CALL db.indexes() YIELD name
    WITH collect(name) AS existingIndexes
    CALL apoc.do.when(
        "dgai_knowledge_vector_index" IN existingIndexes,
        "",
        "CREATE VECTOR INDEX dgai_knowledge_vector_index FOR (n:Document) ON (n.embedding) OPTIONS {indexConfig: { `vector.dimensions`: 1536, `vector.similarity_function`: 'cosine' }};",
        {}
    ) YIELD value RETURN value;
    """,
    """
    CALL db.indexes() YIELD name
    WITH collect(name) AS existingIndexes
    CALL apoc.do.when(
        "dgai_knowledge_entity_index" IN existingIndexes,
        "",
        "CREATE INDEX dgai_knowledge_entity_index FOR (n:Entity) ON (n.id);",
        {}
    ) YIELD value RETURN value;
    """
]

def create_indexes(driver):
    """Function to create required indexes in Neo4j if they do not already exist."""
    with driver.session() as session:
        for query in INDEX_QUERIES:
            try:
                session.run(query)
                print(f"✅ Index checked/created successfully.")
            except Exception as e:
                print(f"⚠️ Skipping index creation due to: {e}")

# Connect to Neo4j
driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))

# Ensure indexes exist before running retrieval
create_indexes(driver)

# Close connection
driver.close()



OR MANUALLY
CREATE FULLTEXT INDEX IF NOT EXISTS dgai_knowledge_text_index
FOR (n:Document)
ON EACH [n.text, n.category, n.document_type, n.legal_entities, n.publisher, n.regulator, n.regulatory_reporting_obligation];

CREATE VECTOR INDEX IF NOT EXISTS dgai_knowledge_vector_index
FOR (n:Document)
ON (n.embedding)
OPTIONS {indexConfig: { `vector.dimensions`: 1536, `vector.similarity_function`: 'cosine' }};

CREATE INDEX IF NOT EXISTS dgai_knowledge_entity_index
FOR (n:Entity)
ON (n.id);


DROP UNNECESSARY
DROP INDEX keyword;
DROP INDEX vector_index;
DROP INDEX vector;
