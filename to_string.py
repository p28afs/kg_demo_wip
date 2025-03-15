def to_string(value):
    """
    Recursively convert a value to a string.
    - If the value is already a string, return it.
    - If it is a list, recursively convert each element and join them with a space.
    - If it is a dictionary, recursively process its key/value pairs.
    - Otherwise, convert it using str().
    """
    if isinstance(value, str):
        return value
    elif isinstance(value, list):
        # Convert each element to string and join them
        return " ".join(to_string(item) for item in value)
    elif isinstance(value, dict):
        # Optionally, you can recursively convert dictionary values into strings.
        # Here, we simply convert the dictionary itself to a JSON-style string.
        # Alternatively, you could process each key/value pair.
        return "{" + ", ".join(f"{k}: {to_string(v)}" for k, v in value.items()) + "}"
    else:
        return str(value)

def convert_properties_to_string(properties: dict) -> dict:
    """
    Takes a dictionary of properties and returns a new dictionary where every value is a string.
    """
    return {key: to_string(val) for key, val in properties.items()}

# Example usage:
sample_properties = {
    "title": ["Understanding", "Neo4j", "Graph", "Embeddings"],
    "abstract": "This document explains how to use Neo4jVector.from_existing_graph.",
    "year": 2024,
    "metadata": {"author": ["Alice", "Bob"], "pages": 10}
}

converted = convert_properties_to_string(sample_properties)
print(converted)
