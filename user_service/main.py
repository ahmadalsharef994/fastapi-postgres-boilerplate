# user_service/main.py

from fastapi import FastAPI
from .routes import user
from .database import init_db

app = FastAPI(title="User Service")

app.include_router(user.router, prefix="/user")

@app.on_event("startup")
async def startup():
    await init_db()
