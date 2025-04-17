import random
import json
import os
from docx import Document
import PyPDF2

def extract_text_from_docx(path):
    doc = Document(path)
    return "\n".join([para.text for para in doc.paragraphs])

def extract_text_from_pdf(path):
    text = ""
    with open(path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text() + "\n"
    return text

def extract_text_from_txt(path):
    with open(path, 'r', encoding='utf-8') as file:
        return file.read()

def get_random_phrases(text, min_words=5, max_words=10, num_phrases=10):
    words = text.split()
    phrases = []
    for _ in range(num_phrases):
        if len(words) < min_words:
            break
        start = random.randint(0, len(words) - min_words)
        end = min(start + random.randint(min_words, max_words), len(words))
        phrases.append(" ".join(words[start:end]))
    return phrases

def extract_phrases(file_path, output_path="D:/prag-check/backend/utils/phrases.json"):
    # Ensure the directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    ext = os.path.splitext(file_path)[1].lower()
    if ext == ".docx":
        text = extract_text_from_docx(file_path)
    elif ext == ".pdf":
        text = extract_text_from_pdf(file_path)
    elif ext == ".txt":
        text = extract_text_from_txt(file_path)
    else:
        raise ValueError("Unsupported file type: must be .docx, .pdf or .txt")

    phrases = get_random_phrases(text)
    
    # Save phrases to the specified output path
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(phrases, f, indent=4)

    return phrases
