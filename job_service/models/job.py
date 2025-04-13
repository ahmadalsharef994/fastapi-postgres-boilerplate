from job_service.db import Base
from sqlalchemy import Column, Integer, String

class Job(Base):
    __tablename__ = "jobs"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    location = Column(String)
