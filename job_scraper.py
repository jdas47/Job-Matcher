def generate_search_links(skills):
    job_links = []
    for skill in skills:
        links = {
            "Internshala": f"https://internshala.com/internships/keywords-{skill}/",
            "Naukri": f"https://www.naukri.com/{skill}-jobs",
            "Unstop": f"https://unstop.com/opportunities?search={skill}",
            "LinkedIn": f"https://www.linkedin.com/jobs/search/?keywords={skill}"
        }
        job_links.append((skill, links))
    return job_links
