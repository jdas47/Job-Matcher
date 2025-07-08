import requests
import os

RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY", "YOUR_RAPIDAPI_KEY")

def generate_search_links(skills, location, job_type, remote_option):
    job_links = []

    for skill in skills:
        loc_query = f"+{location}" if location else ""

        links = {
            "Internshala": f"https://internshala.com/internships/keywords-{skill}{('-' + location.lower().replace(' ', '-')) if location else ''}/",
            "Naukri": f"https://www.naukri.com/{skill}-jobs-in-{location.lower().replace(' ', '-')}" if location else f"https://www.naukri.com/{skill}-jobs",
            "Unstop": f"https://unstop.com/opportunities?search={skill}%20{location}" if location else f"https://unstop.com/opportunities?search={skill}",
            "LinkedIn": f"https://www.linkedin.com/jobs/search/?keywords={skill}{('%20' + location) if location else ''}"
        }

        job_links.append((skill, links))

    return job_links

def fetch_live_jobs(skill, location=""):
    """
    Calls JSearch API on RapidAPI to get live job listings.
    """
    if RAPIDAPI_KEY == "34614dec21mshf880c03f6ca600dp1a6382jsn27c7f3eccf8e":
        return []

    url = "https://jsearch.p.rapidapi.com/search"

    querystring = {
        "query": f"{skill} {location}".strip(),
        "page": "1",
        "num_pages": "1"
    }

    headers = {
        "X-RapidAPI-Key": RAPIDAPI_KEY,
        "X-RapidAPI-Host": "jsearch.p.rapidapi.com"
    }

    try:
        response = requests.get(url, headers=headers, params=querystring)
        response.raise_for_status()

        data = response.json()
        jobs = []

        for job in data.get("data", []):
            jobs.append({
                "title": job.get("job_title", ""),
                "company": job.get("employer_name", ""),
                "location": job.get("job_city", ""),
                "url": job.get("job_apply_link", "")
            })

        return jobs

    except requests.RequestException as e:
        print(f"API Error: {e}")
        return []
