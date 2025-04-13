# --- app/routes/hello.py ---
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def hello():
    return {"message": "Welcome to SmartHub Boilerplate!"}
