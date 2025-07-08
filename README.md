# 💼 Job Matcher

A Streamlit web app that helps job seekers instantly discover job opportunities based on the skills detected in their resume.
[Live App](https://job-matcher-96j4kalzteevpmwbqgv9in.streamlit.app/)
---

## 🚀 Features

✅ Upload your resume in PDF or Excel format  
✅ Extracts your skills automatically using NLP (spaCy)  
✅ Searches for matching jobs on:
- Internshala
- Naukri
- Unstop
- LinkedIn

✅ Provides direct clickable links to relevant job listings  
✅ Runs completely in your browser

---

## 🔧 How It Works

1. Upload your resume (PDF or Excel)
2. App extracts text and identifies popular technical skills
3. App generates job search links for each detected skill
4. Click the links and start applying for jobs!

---

## 📁 Project Structure

Job-Matcher/
├── app.py
├── resume_parser.py
├── job_scraper.py
├── requirements.txt


---

## ⚙️ Installation

Clone this repository:

```bash
git clone https://github.com/jdas47/Job-Matcher.git
cd resume-Job-Matcher
```

Install dependencies:
```
pip install -r requirements.txt
```
Download spaCy language model:
```
python -m spacy download en_core_web_sm
```

Run the App Locally
```
streamlit run app.py
```

🛠 Dependencies
```
streamlit
pymupdf
pandas
openpyxl
```
Check requirements.txt for details.
 









