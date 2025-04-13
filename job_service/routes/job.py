from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from ..db import get_db
# import from 1 level up?



from ..models.job import Job

router = APIRouter(prefix="/jobs", tags=["Jobs"])

@router.post("/")
def create_job(title: str, description: str, location: str, db: Session = Depends(get_db)):
    job = Job(title=title, description=description, location=location)
    db.add(job)
    db.commit()
    db.refresh(job)
    return job

@router.get("/{job_id}")
def get_job(job_id: int, db: Session = Depends(get_db)):
    job = db.query(Job).filter(Job.id == job_id).first()
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    return job
