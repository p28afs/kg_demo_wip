import streamlit as st
from pages import upload, search

# Set page layout
st.set_page_config(page_title="GraphRAG Search", layout="wide")

st.title("📚 GraphRAG Search")

# Upload Section
st.header("📤 Upload Documents")
upload.show()

st.markdown("---")

# Search Section
st.header("🔎 Semantic Search")
search.show()
