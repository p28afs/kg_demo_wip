import streamlit as st
from pyvis.network import Network
import streamlit.components.v1 as components

# Mock graph data simulating Neo4j query output
# Format: [(from_node, relation, to_node), ...]
graph_data = [
    ("Trade", "REPORTED_BY", "ReportingCounterparty"),
    ("Trade", "REPORTED_TO", "TradeRepository"),
    ("Trade", "INVOLVES", "Counterparty1"),
    ("Trade", "INVOLVES", "Counterparty2"),
    ("Trade", "HAS", "Product"),
    ("Product", "CLASSIFIED_AS", "AssetClass"),
    ("Trade", "TRADED_ON", "ExecutionVenue"),
    ("Trade", "CLEARED_BY", "CCP"),
    ("ReportingCounterparty", "IS", "FinancialCounterparty"),
    ("ReportingCounterparty", "LOCATED_IN", "EU"),
    ("Counterparty1", "IS", "NonFinancialCounterparty"),
    ("Counterparty2", "IS", "FinancialCounterparty"),
    ("TradeRepository", "REGULATED_BY", "ESMA"),
    ("Trade", "SUBJECT_TO", "EMIR_3.0"),
    ("EMIR_3.0", "DEFINED_BY", "ESMA"),
    ("Trade", "HAS", "UTI"),
    ("UTI", "ASSIGNED_BY", "ReportingCounterparty"),
    ("Trade", "HAS", "Valuation"),
    ("Valuation", "PROVIDED_BY", "ValuationProvider"),
    ("ValuationProvider", "IS", "FinancialCounterparty"),
    ("Trade", "HAS", "Collateral"),
    ("Collateral", "POSTED_BY", "Counterparty1"),
    ("Collateral", "RECEIVED_BY", "Counterparty2"),
]
def visualize_graph(data):
    net = Network(height="600px", width="100%", directed=True)
    for from_node, relation, to_node in data:
        net.add_node(from_node, label=from_node)
        net.add_node(to_node, label=to_node)
        net.add_edge(from_node, to_node, label=relation)

    return net.generate_html()

# Streamlit UI
st.title("Example Knowledge Graph Viewer")

if graph_data:
    html_graph = visualize_graph(graph_data)
    components.html(html_graph, height=600, scrolling=True)
else:
    st.write("No graph data to display.")
