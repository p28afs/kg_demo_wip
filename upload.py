import streamlit as st
import os
import time
import json
import pandas as pd
from datetime import datetime

# Path to store uploaded documents
DOCS_DIR = "docs"

# Ensure docs directory exists
os.makedirs(DOCS_DIR, exist_ok=True)


# Load existing uploaded files
def load_uploaded_files():
    files_data = []

    for category in os.listdir(DOCS_DIR):
        category_path = os.path.join(DOCS_DIR, category)
        if os.path.isdir(category_path):  # Ensure it's a category folder
            for filename in os.listdir(category_path):
                if filename.endswith(".pdf"):  # Look for PDF files
                    pdf_path = os.path.join(category_path, filename)
                    meta_path = pdf_path.replace(".pdf", "_metadata.json")

                    if os.path.exists(meta_path):  # Ensure metadata exists
                        with open(meta_path, "r") as meta_file:
                            metadata = json.load(meta_file)
                    else:
                        metadata = {}

                    files_data.append({
                        "Knowledge Identifier": metadata.get("id", "Unknown"),
                        "Category": category,
                        "Doc Name": filename,
                        "Doc Version": metadata.get("version", "1.0"),
                        "Metadata": str(metadata),
                        "User": metadata.get("user", "Unknown"),
                        "Timestamp": metadata.get("timestamp", "Unknown"),
                        "Path": pdf_path  # Store path for deletion
                    })

    return pd.DataFrame(files_data)


# Save uploaded file
def save_uploaded_file(category, pdf_file, meta_file):
    category_path = os.path.join(DOCS_DIR, category)
    os.makedirs(category_path, exist_ok=True)

    pdf_path = os.path.join(category_path, pdf_file.name)
    meta_path = pdf_path.replace(".pdf", "_metadata.json")

    # Save PDF file
    with open(pdf_path, "wb") as f:
        f.write(pdf_file.getbuffer())

    # Save metadata file
    meta_data = json.load(meta_file)
    meta_data["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Add timestamp

    with open(meta_path, "w") as f:
        json.dump(meta_data, f, indent=4)


# Remove a document
def remove_document(doc_path):
    meta_path = doc_path.replace(".pdf", "_metadata.json")

    if os.path.exists(doc_path):
        os.remove(doc_path)

    if os.path.exists(meta_path):
        os.remove(meta_path)

    # Remove the category folder if empty
    category_path = os.path.dirname(doc_path)
    if not os.listdir(category_path):
        os.rmdir(category_path)


def show():
    st.subheader("📂 Uploaded Documents")

    # Load and display existing uploaded files
    if "uploaded_files" not in st.session_state:
        st.session_state.uploaded_files = load_uploaded_files()

    df = st.session_state.uploaded_files
    if df.empty:
        st.info("No documents uploaded yet.")
    else:
        # Display table with remove button
        for i in range(len(df)):
            col1, col2, col3, col4, col5, col6, col7, remove_col = st.columns(8)

            col1.write(df.iloc[i]["Knowledge Identifier"])
            col2.write(df.iloc[i]["Category"])
            col3.write(df.iloc[i]["Doc Name"])
            col4.write(df.iloc[i]["Doc Version"])
            col5.write(df.iloc[i]["Metadata"])
            col6.write(df.iloc[i]["User"])
            col7.write(df.iloc[i]["Timestamp"])

            if remove_col.button("❌", key=f"remove_{i}"):
                remove_document(df.iloc[i]["Path"])
                st.session_state.uploaded_files = load_uploaded_files()
                st.experimental_rerun()

    st.markdown("---")

    # File Upload Section
    st.subheader("➕ Add a Document")

    category = st.text_input("Category (e.g., Finance, Research, Legal)")
    pdf_file = st.file_uploader("Upload PDF Document", type=["pdf"])
    meta_file = st.file_uploader("Upload Metadata File (JSON)", type=["json"])

    if st.button("Upload"):
        if pdf_file and meta_file and category:
            file_size_kb = len(pdf_file.getbuffer()) / 1024
            progress_bar = st.progress(0)

            for i in range(int(file_size_kb / 100) + 1):
                time.sleep(1)  # Simulate processing time
                progress_bar.progress(min((i + 1) * 10, 100))

            save_uploaded_file(category, pdf_file, meta_file)

            st.success(f"✅ {pdf_file.name} uploaded successfully!")
            st.session_state.uploaded_files = load_uploaded_files()
            st.experimental_rerun()
        else:
            st.warning("⚠️ Please provide a category and upload both a PDF and a metadata file.")
