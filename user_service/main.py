from fastapi import FastAPI
from user_service.routes import user

app = FastAPI()
app.include_router(user.router)
