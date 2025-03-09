import streamlit as st
import time

def show():
    # Search Configurations (Moved above the search box)
    st.subheader("⚙️ Search Configuration")

    node_limit = st.slider("Node Limit (max graph depth)", min_value=1, max_value=10, value=2, step=1)
    relevancy_score = st.slider("Relevancy Score Threshold", min_value=0.0, max_value=1.0, value=0.9, step=0.05)
    k = st.slider("Number of Documents (k)", min_value=1, max_value=20, value=4, step=1)

    # Search Input Field
    query = st.text_input("Enter your search query")

    if "search_results" not in st.session_state:
        st.session_state.search_results = None  # Initialize session state

    if st.button("Search"):
        if query:
            with st.spinner("🔄 Searching... Please wait (~1 min)"):
                time.sleep(5)  # Simulate delay

            # Dummy RAG results (uses k and relevancy_score)
            rag_result = {
                "answer": "This is a RAG-generated answer.",
                "sources": [
                    {"doc_name": "document1.pdf", "page_number": 3, "content": "This is a sample text from doc1."},
                    {"doc_name": "document2.pdf", "page_number": 7, "content": "This is another sample text from doc2."}
                ][:k],  # Limit based on user input
                "accuracy": f"{int(relevancy_score * 100)}%",  # Fake accuracy based on relevancy score
                "completeness": "80%"
            }

            # Dummy GraphRAG results (uses node_limit)
            graph_rag_result = {
                "answer": f"This is a GraphRAG-generated answer with knowledge graph using {node_limit} nodes.",
                "sources": [
                    {"doc_name": "document1.pdf", "page_number": 3, "content": "This is an enhanced text from doc1."},
                    {"doc_name": "document2.pdf", "page_number": 7, "content": "This is an enhanced text from doc2."}
                ][:k],  # Limit based on user input
                "accuracy": f"{int(relevancy_score * 100) + 5}%",  # Fake accuracy based on relevancy score
                "completeness": "85%"
            }

            # Store results in session state
            st.session_state.search_results = {"rag": rag_result, "graph_rag": graph_rag_result}

    # Display results only if they exist in session state
    if st.session_state.search_results:
        rag_result = st.session_state.search_results["rag"]
        graph_rag_result = st.session_state.search_results["graph_rag"]

        # Layout: Two columns for comparison
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("🔎 RAG Result")
            st.write(f"**Answer:** {rag_result['answer']}")
            st.write("**Sources:**")
            for source in rag_result["sources"]:
                with st.expander(f"{source['doc_name']} (Page {source['page_number']})"):
                    st.write(source["content"])

        with col2:
            st.subheader("🌐 GraphRAG Result")
            st.write(f"**Answer:** {graph_rag_result['answer']}")
            st.write("**Sources:**")
            for source in graph_rag_result["sources"]:
                with st.expander(f"{source['doc_name']} (Page {source['page_number']})"):
                    st.write(source["content"])

            # Graph Visualization Placeholder
            st.subheader("📌 Knowledge Graph")
            st.image("assets/neo4j_graph.png")  # Placeholder image

        # Benchmarking Section
        st.subheader("📊 Benchmarking Comparison")
        st.write(f"**Accuracy:** RAG: {rag_result['accuracy']} | GraphRAG: {graph_rag_result['accuracy']}")
        st.write(f"**Completeness:** RAG: {rag_result['completeness']} | GraphRAG: {graph_rag_result['completeness']}")

        st.markdown("[📩 Provide Feedback](https://example.com/feedback)")
