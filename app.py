import os
import streamlit as st
from resume_parser import extract_text_from_pdf, extract_text_from_excel, extract_skills
from job_scraper import generate_search_links

# Download's spaCy model on deployment
os.system("python -m spacy download en_core_web_sm")

# Page settings 
st.set_page_config(
    page_title="Resume Job Matcher",
    page_icon="💼",
    layout="centered"
)

st.title("💼 Resume Job Matcher")

uploaded_file = st.file_uploader(
    "Upload your resume (PDF or Excel)",
    type=["pdf", "xlsx", "xls"]
)

if uploaded_file:
    if uploaded_file.name.endswith(".pdf"):
        file_bytes = uploaded_file.read()
        text = extract_text_from_pdf(file_bytes)
    else:
        text = extract_text_from_excel(uploaded_file)

    skills = extract_skills(text)

    if skills:
        st.success("✅ Skills Found:")
        st.write(skills)

        job_links = generate_search_links(skills)

        st.header("🔗 Job Search Links")
        for skill, links in job_links:
            st.subheader(f"🔎 Jobs for: {skill}")
            for platform, link in links.items():
                st.markdown(f"- [{platform}]({link})")
    else:
        st.warning("⚠️ No known skills found in your resume.")
