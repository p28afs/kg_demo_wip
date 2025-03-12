import streamlit as st
import pandas as pd
from pathlib import Path
import os

def show_existing_knowledge():
    st.markdown("<h3 style='font-size:24px'>Existing Knowledge</h3>", unsafe_allow_html=True)

    base_path = Path(__file__).resolve().parent.parent.parent / "data"
    prefix_root = "dgai.knowledge.assistant.gtr.regulatory"
    namespaces = ["dgai.knowledge.assistant.gtr.regulatory.emir", "dgai.knowledge.assistant.gtr.regulatory.docs"]

    for namespace in namespaces:
        with st.expander(f"+ {namespace}"):
            # Simulating metadata retrieval
            metadata = [
                {
                    "doc_name": "sample regulatory text.pdf",
                    "doc_version": "1.0",
                    "category": "EMIR3 Validation Rules",
                    "super_department": "Operations Technology",
                    "department": "Transaction Reporting",
                    "timestamp": "2025-03-12 11:05:52",
                    "doc_path": os.path.join(base_path, "sample regulatory text.pdf"),
                    "meta_path": os.path.join(base_path, "sample metadata.txt"),
                },
                {
                    "doc_name": "sample_regulatory_text_2.pdf",
                    "doc_version": "1.0",
                    "category": "EMIR3 Validation Rules",
                    "super_department": "Operations Technology",
                    "department": "Transaction Reporting",
                    "timestamp": "2025-03-12 10:53:49",
                    "doc_path": os.path.join(base_path, "sample_regulatory_text_2.pdf"),
                    "meta_path": os.path.join(base_path, "sample_metadata_2.txt"),
                },
            ]

            if metadata:
                df = pd.DataFrame(metadata)
                st.markdown("<h3 style='font-size:20px'>Stored Documents</h3>", unsafe_allow_html=True)

                # Display Markdown Table Headers
                headers = "| doc_name | doc_version | category | super_department | department | timestamp | Download |"
                separator = "|----------|------------|----------|------------------|------------|------------|----------|"
                st.markdown(headers)
                st.markdown(separator)

                # Render each row dynamically
                for _, row in df.iterrows():
                    # Read the file content for the download button
                    with open(row["doc_path"], "rb") as doc_file:
                        doc_data = doc_file.read()
                    with open(row["meta_path"], "rb") as meta_file:
                        meta_data = meta_file.read()

                    # Create download buttons
                    doc_button = st.download_button(label="📄 Doc", data=doc_data, file_name=row["doc_name"], key=f"doc_{row['doc_name']}")
                    meta_button = st.download_button(label="📑 Meta", data=meta_data, file_name=row["meta_path"], key=f"meta_{row['meta_path']}")

                    # Render row using Markdown for text, but buttons for downloads
                    row_markdown = f"| {row['doc_name']} | {row['doc_version']} | {row['category']} | {row['super_department']} | {row['department']} | {row['timestamp']} | {doc_button} {meta_button} |"
                    st.markdown(row_markdown, unsafe_allow_html=True)
    st.success("✅ Process completed!")
