from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title="Autonomous Insurance Claims Processing Agent",
    version="1.0.0"
)

app.include_router(router)