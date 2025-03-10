import streamlit as st

# Set page configuration
st.set_page_config(page_title="GraphRAG Knowledge Centre", layout="wide")

# Custom Styling for Icons and Headers
st.markdown("""
    <style>
        .icon-header {
            font-size: 22px;
            font-weight: bold;
            display: flex;
            align-items: center;
            gap: 10px;
        }
        .icon {
            font-size: 24px;
            color: #4A90E2;
        }
    </style>
""", unsafe_allow_html=True)

# Title with Icon
st.markdown("<h1 style='text-align: center;'>📚 GraphRAG Knowledge Centre</h1>", unsafe_allow_html=True)

# Subheader: Add New Knowledge
st.markdown("<div class='icon-header'>🆕 Add New Knowledge</div>", unsafe_allow_html=True)

# File Upload Inputs
doc_file = st.file_uploader("Choose a knowledge document file", type=["pdf", "docx", "txt", "xls", "xlsx"])
meta_file = st.file_uploader("Choose a metadata file", type=["json"])

if st.button("Upload Files"):
    st.success("Files uploaded successfully!")

st.markdown("---")  # Separator

# Subheader: Existing Knowledge
st.markdown("<div class='icon-header'>📂 Existing Knowledge</div>", unsafe_allow_html=True)

# Expandable Sections for Documents
with st.expander("📜 dgai.knowledge.assistant.gtr.regulatory.docs"):
    st.write("Stored documents will be displayed here.")

with st.expander("📜 dgai.knowledge.assistant.gtr.qaem.docs"):
    st.write("Stored documents will be displayed here.")
