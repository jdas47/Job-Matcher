import os
import fitz  # PyMuPDF
import spacy
import pandas as pd

_spacy_model = None

SKILL_LIST = [
    "python", "java", "c++", "html", "css", "javascript",
    "sql", "react", "node", "django", "flask", "data analysis",
    "machine learning", "deep learning", "nlp", "excel"
]

def extract_text_from_pdf(file_bytes):
    """
    Extract text from a PDF file uploaded as bytes.
    """
    text = ""
    with fitz.open(stream=file_bytes, filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()
    return text

def extract_text_from_excel(uploaded_file):
    """
    Extract all cell contents from an uploaded Excel file as plain text.
    """
    df = pd.read_excel(uploaded_file)
    text = " ".join(df.astype(str).fillna("").values.flatten())
    return text

def extract_skills(text):
    """
    Detect skills from text using spaCy NLP model.
    """
    global _spacy_model
    if _spacy_model is None:
        _spacy_model = spacy.load("en_core_web_sm")
    doc = _spacy_model(text.lower())
    found_skills = set()
    for token in doc:
        if token.text in SKILL_LIST:
            found_skills.add(token.text)
    return list(found_skills)
