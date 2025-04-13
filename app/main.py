# --- app/main.py ---
from fastapi import FastAPI
from app.routes.hello import router as hello_router
from app.db.database import init_db

app = FastAPI(title="SmartHub Boilerplate")

app.include_router(hello_router)

@app.on_event("startup")
def startup():
    init_db()
