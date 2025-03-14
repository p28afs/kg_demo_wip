import streamlit as st
import time

def update_callback(message, status=None):
    if status:
        status.update(label=message, state="running")  # Update ongoing process
    else:
        st.write(message)  # Fallback for non-status updates

def long_running_process():
    with st.status("Starting process...", expanded=True) as status:
        update_callback("Step 1: Fetching data...", status)
        time.sleep(5)  # Simulating a long-running step

        update_callback("Step 2: Processing embeddings...", status)
        time.sleep(10)

        update_callback("Step 3: Storing results in Neo4j...", status)
        time.sleep(7)

        update_callback("✅ Process completed successfully!", status)
        status.update(label="✅ All steps completed!", state="complete")

# Run the process on button click
if st.button("Run Process"):
    long_running_process()
