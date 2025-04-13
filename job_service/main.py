# --- job_service/main.py ---
from fastapi import FastAPI
from routes import job

app = FastAPI()
app.include_router(job.router)