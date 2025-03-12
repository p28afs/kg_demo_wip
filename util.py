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
                # Create a DataFrame to display in a table format
                df = pd.DataFrame(metadata)
                st.markdown("<h3 style='font-size:20px'>Stored Documents</h3>", unsafe_allow_html=True)

                # Add a new column for download links
                df["Download"] = df.apply(lambda row: f"[doc](file://{row['doc_path']}) [meta](file://{row['meta_path']})", axis=1)

                # Display the table with the new column
                for _, row in df.iterrows():
    doc_link = f"[doc](file://{row['doc_path']})"
    meta_link = f"[meta](file://{row['meta_path']})"

    # Render table row using Markdown to ensure clickable links
    st.markdown(
        f"| {row['doc_name']} | {row['doc_version']} | {row['category']} | {row['super_department']} | {row['department']} | {row['timestamp']} | {doc_link} {meta_link} |",
        unsafe_allow_html=True
    )

