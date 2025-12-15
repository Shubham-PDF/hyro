from PyPDF2 import PdfReader
import io
import re

def extract_resume_text(file_bytes):
    try:
        
        pdf_file = io.BytesIO(file_bytes)
        pdf_reader = PdfReader(pdf_file)
        text = ""

        for page in pdf_reader.pages:
            extracted = page.extract_text()
            if extracted:
                text += extracted

        return clean_text(text)

    except Exception as e:
        
        print(f"PDF extract error: {e}")
        return ""


def clean_text(text):
    text = text.lower()
    # Replace newlines with spaces to prevent words breaking across lines
    text = text.replace('\n', ' ') 
    # Remove special characters but keep numbers and spaces
    text = re.sub(r'[^a-z0-9\s]', '', text) 
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text)
    return text.strip()


def compute_match_score(text, keywords):
    if not keywords:
        return 0

    # Convert text to a set of words for O(1) lookups and exact matching
    # This prevents "Java" matching "Javascript"
    text_words = set(text.split())
    
    match_count = 0
    for kw in keywords:
        kw_clean = kw.lower()
        # Check if the exact keyword exists in the set of words
        # OR check if multi-word keyword (e.g., "machine learning") is in the string
        if " " in kw_clean:
             if kw_clean in text:
                 match_count += 1
        elif kw_clean in text_words:
            match_count += 1

    return round((match_count / len(keywords)) * 100, 2)