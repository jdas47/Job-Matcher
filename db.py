from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
import datetime
import json

Base = declarative_base()

class SearchHistory(Base):
    __tablename__ = "history"

    id = Column(Integer, primary_key=True)
    email = Column(String(255))
    resume_filename = Column(String(255))
    skills = Column(Text)
    location = Column(String(255))
    job_type = Column(String(255))
    remote_option = Column(String(255))
    job_links = Column(Text)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)

engine = create_engine("sqlite:///history.db")
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

def save_history(email, filename, skills, location, job_type, remote_option, job_links):
    session = Session()
    history = SearchHistory(
        email=email,
        resume_filename=filename,
        skills=json.dumps(skills),
        location=location,
        job_type=job_type,
        remote_option=remote_option,
        job_links=json.dumps(job_links)
    )
    session.add(history)
    session.commit()
    session.close()

def load_history(email):
    session = Session()
    rows = session.query(SearchHistory).filter_by(email=email).all()
    session.close()
    return rows
