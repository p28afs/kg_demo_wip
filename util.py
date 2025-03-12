import streamlit as st
import pandas as pd
from pathlib import Path

def show_existing_knowledge():
    st.markdown("<h3 style='font-size:24px'>Existing Knowledge</h3>", unsafe_allow_html=True)

    base_path = Path(__file__).resolve().parent.parent.parent / DATA_DIR
    prefix_root = NAMESPACE_PREFIX.split("/")[0]
    namespaces = get_namespaces(base_path, prefix_root)

    for namespace in namespaces:
        with st.expander(f"+ {namespace}"):
            metadata = read_metadata(base_path, namespace)
            if metadata:
                # Convert metadata to DataFrame
                df = pd.DataFrame(metadata)

                # Add Download Doc & Metadata columns
                df["Download Doc"] = ""
                df["Download Metadata"] = ""

                # Display Table Headers
                st.markdown("<h3 style='font-size:20px'>Stored Documents</h3>", unsafe_allow_html=True)
                table_headers = ["doc_name", "doc_version", "category", "super_department", "department", "timestamp", "Download Doc", "Download Metadata"]
                st.markdown(f"| {' | '.join(table_headers)} |")
                st.markdown(f"| {' | '.join(['---'] * len(table_headers))} |")

                # Create table rows with download buttons
                for index, item in df.iterrows():
                    doc_file_download_key = f"{namespace}_{item['doc_name']}_doc_download"
                    meta_file_download_key = f"{namespace}_{item['doc_name']}_meta_download"

                    # Read file data
                    with open(item['doc_path'], "rb") as f:
                        doc_data = f.read()
                    with open(item['meta_path'], "rb") as f:
                        meta_data = f.read()

                    # Display Row with Download Buttons
                    row_values = [
                        item['doc_name'],
                        item['doc_version'],
                        item['category'],
                        item['super_department'],
                        item['department'],
                        item['timestamp'],
                        st.download_button(label="Download Doc", data=doc_data, file_name=item['doc_name'], key=doc_file_download_key),
                        st.download_button(label="Download Metadata", data=meta_data, file_name=item['meta_path'], key=meta_file_download_key)
                    ]

                    # Convert row to Markdown to maintain formatting
                    row_markdown = "| " + " | ".join(str(v) for v in row_values) + " |"
                    st.markdown(row_markdown, unsafe_allow_html=True)

