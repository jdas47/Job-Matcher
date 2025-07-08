import fitz  # PyMuPDF
import pandas as pd
import re

SKILL_LIST = [
    "python", "java", "c++", "html", "css", "javascript",
    "sql", "react", "node", "django", "flask", "data analysis",
    "machine learning", "deep learning", "nlp", "excel"
]

def extract_text_from_pdf(file_bytes):
    """
    Extract text from PDF bytes.
    """
    text = ""
    with fitz.open(stream=file_bytes, filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()
    return text

def extract_text_from_excel(uploaded_file):
    """
    Extract text from Excel file.
    """
    df = pd.read_excel(uploaded_file)
    text = " ".join(df.astype(str).fillna("").values.flatten())
    return text

def extract_skills(text):
    """
    Extract skills from text using pure Python.
    """
    # Lowercase and split words
    words = re.findall(r'\w+', text.lower())

    found_skills = set()
    for skill in SKILL_LIST:
        if " " in skill:
            if skill in text.lower():
                found_skills.add(skill)
        else:
            if skill in words:
                found_skills.add(skill)

    return list(found_skills)
