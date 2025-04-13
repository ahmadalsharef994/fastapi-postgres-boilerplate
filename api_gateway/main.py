from fastapi import FastAPI
from routes.websocket import router as ws_router
# from routes.users import router as user_router
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()

app.include_router(ws_router)
# app.include_router(user_router)

# Register Prometheus metrics
Instrumentator().instrument(app).expose(app)