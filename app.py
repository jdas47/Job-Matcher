import streamlit as st
from resume_parser import (
    extract_text_from_pdf,
    extract_text_from_excel,
    extract_skills,
    suggest_skills,
)
from job_scraper import generate_search_links
from db import save_history, load_history
import json

st.title("🎯 Resume Job Matcher")

# Sidebar for viewing history
if st.sidebar.checkbox("View My Previous Searches"):
    user_email = st.sidebar.text_input("Enter your email to load your history:")

    if user_email and st.sidebar.button("Load History"):
        rows = load_history(user_email)

        if rows:
            st.header("🔎 Your Previous Searches")

            for row in rows:
                st.subheader(f"Resume: {row.resume_filename}")
                st.write(f"Skills: {json.loads(row.skills)}")
                st.write(f"Location: {row.location}")
                st.write(f"Job Type: {row.job_type}")
                st.write(f"Remote Option: {row.remote_option}")
                st.write(f"Timestamp: {row.timestamp}")

                links = json.loads(row.job_links)
                for skill, skill_links in links:
                    st.markdown(f"**{skill.capitalize()} Jobs:**")
                    for platform, url in skill_links.items():
                        st.markdown(f"- [{platform}]({url})")

                st.markdown("---")
        else:
            st.info("No previous searches found for this email.")

# Filters
st.sidebar.header("Job Search Filters")

location = st.sidebar.text_input("Preferred Location", value="")
job_type = st.sidebar.selectbox(
    "Job Type",
    ["Any", "Internship", "Full-Time", "Freelance", "Part-Time"]
)
remote_option = st.sidebar.selectbox(
    "Work Mode",
    ["Any", "Remote", "Onsite", "Hybrid"]
)

uploaded_file = st.file_uploader("Upload your resume (PDF or Excel)", type=["pdf", "xlsx", "xls"])

if uploaded_file:
    if uploaded_file.name.endswith(".pdf"):
        file_bytes = uploaded_file.read()
        text = extract_text_from_pdf(file_bytes)
    else:
        text = extract_text_from_excel(uploaded_file)

    skills = extract_skills(text)

    if skills:
        st.success("Skills Found:")

        # Colored tags
        st.markdown(" ".join(
            [f"<span style='background-color:#D6EAF8; color:#154360; padding:4px 8px; border-radius:10px; margin-right:4px; font-size:14px'>{skill}</span>"
             for skill in skills]
        ), unsafe_allow_html=True)

        # Chart
        skill_freq = {skill: 1 for skill in skills}
        st.write("### Skill Frequency Chart")
        st.bar_chart(skill_freq)

        # Suggestions
        suggestions = suggest_skills(skills)

        if suggestions:
            st.header("🎯 Resume Improvement Suggestions")
            for domain, missing_skills in suggestions.items():
                st.markdown(f"**For {domain} jobs**, consider adding these skills:")
                st.markdown(", ".join(
                    [f"`{skill}`" for skill in missing_skills]
                ))
        else:
            st.success("✅ Your resume already includes many key skills!")

        # Job Links
        job_links = generate_search_links(skills, location, job_type, remote_option)

        st.header("🔗 Job Search Links")
        for skill, links in job_links:
            st.subheader(f"Jobs for: {skill.capitalize()}")
            for platform, link in links.items():
                st.markdown(f"- [{platform}]({link})")

        # Email Option
        email = st.text_input("Enter your email to receive these job links:")

        if email:
            if st.button("Send Email"):
                from email_sender import send_email
                send_email(email, job_links)
                st.success("✅ Email sent successfully!")

            save_history(
                email=email,
                filename=uploaded_file.name,
                skills=skills,
                location=location,
                job_type=job_type,
                remote_option=remote_option,
                job_links=job_links
            )
    else:
        st.warning("No known skills found in your resume.")
