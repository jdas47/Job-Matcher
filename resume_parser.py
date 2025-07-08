import fitz  # PyMuPDF
import pandas as pd
from rapidfuzz import fuzz
import re

# Skill clusters for feedback
SKILL_CLUSTERS = {
    "Data Science": [
        "python", "pandas", "numpy", "scikit-learn",
        "machine learning", "deep learning", "data analysis"
    ],
    "Web Development": [
        "html", "css", "javascript", "react", "node",
        "django", "flask"
    ],
    "Software Engineering": [
        "java", "c++", "python", "sql", "git"
    ]
}

# Master skill list
SKILL_LIST = sorted(
    set([skill for cluster in SKILL_CLUSTERS.values() for skill in cluster])
)

SYNONYMS = {
    "js": "javascript",
    "ml": "machine learning",
    "ai": "artificial intelligence",
    "py": "python",
    "xls": "excel"
}

def extract_text_from_pdf(file_bytes):
    text = ""
    with fitz.open(stream=file_bytes, filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()
    return text

def extract_text_from_excel(file_obj):
    df = pd.read_excel(file_obj)
    text = " ".join(df.astype(str).fillna("").values.flatten())
    return text

def extract_skills(text):
    words = set(re.findall(r'\w+', text.lower()))
    text_lower = text.lower()

    found_skills = set()

    # check synonyms
    for word in words:
        if word in SYNONYMS:
            found_skills.add(SYNONYMS[word])

    for skill in SKILL_LIST:
        for word in words:
            if fuzz.ratio(skill, word) >= 85:
                found_skills.add(skill)
                break
        if " " in skill and skill in text_lower:
            found_skills.add(skill)

    return list(found_skills)

def suggest_skills(found_skills):
    suggestions = {}

    for domain, domain_skills in SKILL_CLUSTERS.items():
        missing_skills = []
        for skill in domain_skills:
            if skill not in found_skills:
                missing_skills.append(skill)
        if missing_skills and len(missing_skills) < len(domain_skills):
            suggestions[domain] = missing_skills

    return suggestions
