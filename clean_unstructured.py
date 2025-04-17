import re

def clean_for_llm_and_user(raw_content):
    # Step 1: Encode to utf-8
    cleaned = raw_content.encode('utf-8', errors='ignore').decode('utf-8')
    
    # Step 2: Remove control characters but keep readable line breaks
    cleaned = re.sub(r'[\x00-\x08\x0B-\x0C\x0E-\x1F\x7F]', '', cleaned)
    
    # Step 3: Normalize multiple blank lines into one
    cleaned = re.sub(r'\n\s*\n+', '\n\n', cleaned)
    
    # Step 4: Strip leading/trailing whitespace
    cleaned = cleaned.strip()
    
    return cleaned
