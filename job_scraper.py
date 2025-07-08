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
