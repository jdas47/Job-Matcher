import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

SENDER_EMAIL = "YOUR_EMAIL@gmail.com"
APP_PASSWORD = "YOUR_APP_PASSWORD"

def send_email(to_email, job_links):
    message_html = "<h2>Here are your job links:</h2>"
    for skill, links in job_links:
        message_html += f"<h4>{skill.capitalize()}</h4><ul>"
        for platform, url in links.items():
            message_html += f"<li><a href='{url}'>{platform}</a></li>"
        message_html += "</ul>"

    msg = MIMEMultipart("alternative")
    msg["Subject"] = "Your Job Matches from Resume Job Matcher"
    msg["From"] = SENDER_EMAIL
    msg["To"] = to_email

    msg.attach(MIMEText(message_html, "html"))

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(SENDER_EMAIL, APP_PASSWORD)
        server.sendmail(SENDER_EMAIL, to_email, msg.as_string())
