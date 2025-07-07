import os
os.system("python -m spacy download en_core_web_sm")

import fitz  # PyMuPDF
import spacy
import pandas as pd


nlp = spacy.load("en_core_web_sm")

# A sample list of popular skills
SKILL_LIST = [
    "python", "java", "c++", "html", "css", "javascript",
    "sql", "react", "node", "django", "flask", "data analysis",
    "machine learning", "deep learning", "nlp", "excel"
]

def extract_text_from_pdf(file_bytes):
    """
    Takes PDF bytes and extracts text from all pages.
    """
    text = ""
    with fitz.open(stream=file_bytes, filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()
    return text

def extract_text_from_excel(uploaded_file):
    """
    Takes a Streamlit-uploaded Excel file and extracts all text.
    """
    df = pd.read_excel(uploaded_file)
    text = " ".join(df.astype(str).fillna("").values.flatten())
    return text

def extract_skills(text):
    """
    Takes plain text and returns a list of matched skills.
    """
    doc = nlp(text.lower())
    found_skills = set()
    for token in doc:
        if token.text in SKILL_LIST:
            found_skills.add(token.text)
    return list(found_skills)
