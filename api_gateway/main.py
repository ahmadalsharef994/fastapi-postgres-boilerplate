from fastapi import FastAPI
from .routes import auth
from .middlewares.cors import add_cors

app = FastAPI()
add_cors(app)

app.include_router(auth.router, prefix="/auth")
