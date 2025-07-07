import fitz  # PyMuPDF
import spacy
import pandas as pd

_spacy_model = None

SKILL_LIST = [
    "python", "java", "c++", "html", "css", "javascript",
    "sql", "react", "node", "django", "flask", "data analysis",
    "machine learning", "deep learning", "nlp", "excel"
]

def load_spacy_model():
    """
    Dynamically download spaCy model if missing.
    Works on any environment, including Streamlit Cloud.
    """
    global _spacy_model
    if _spacy_model is None:
        try:
            _spacy_model = spacy.load("en_core_web_sm")
        except OSError:
            # Download if not present
            from spacy.cli import download
            download("en_core_web_sm")
            _spacy_model = spacy.load("en_core_web_sm")
    return _spacy_model

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
    Find skills in text using spaCy and a predefined skill list.
    """
    nlp = load_spacy_model()
    doc = nlp(text.lower())
    found_skills = set()
    for token in doc:
        if token.text in SKILL_LIST:
            found_skills.add(token.text)
    return list(found_skills)
