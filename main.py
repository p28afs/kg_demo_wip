import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(page_title="GraphRAG Experimental", layout="wide")

# Title
st.markdown("<h1 style='text-align: center;'>GraphRAG Knowledge Centre</h1>", unsafe_allow_html=True)

# Expandable Section Function
def expandable_section(title, data=None):
    with st.expander(f"➕ {title}"):
        if data is not None:
            st.markdown("<h3 style='font-size:20px;'>Stored Documents</h3>", unsafe_allow_html=True)
            st.table(data)
        else:
            st.markdown("No documents uploaded yet.")


with st.container():
    st.markdown("<h3 style='font-size:24px; font-weight:bold;'>Submit New Knowledge</h3>", unsafe_allow_html=True)

    # File Upload Inputs
    doc_file = st.file_uploader("Choose a knowledge document file", type=["pdf", "docx", "txt", "xls", "xlsx"])
    meta_file = st.file_uploader("Choose a metadata file", type=["json"])

    if st.button("Upload Files"):
        st.success("Files uploaded successfully!")

st.markdown("---")

st.markdown("<h3 style='font-size:24px; font-weight:bold;'>Existing Knowledge</h3>", unsafe_allow_html=True)
# Example Table Data
data_regulatory = pd.DataFrame({
    "Filename": ["Regulatory_Doc1.pdf", "Regulatory_Doc2.xlsx"],
    "Size": ["2MB", "5MB"],
    "Uploaded By": ["User1", "User2"],
    "Date": ["2025-03-10", "2025-03-09"]
})

# Expandable Table
expandable_section("dgai.knowledge.assistant.gtr.regulatory.docs", data_regulatory)


# Example Table Data for QAEM
data_qaem = pd.DataFrame({
    "Filename": [],
    "Size": [],
    "Uploaded By": [],
    "Date": []
})

expandable_section("dgai.knowledge.assistant.gtr.qaem.docs", data_qaem)
