from fastapi import FastAPI
from app.routes.execution_routes import router

app = FastAPI()
app.include_router(router, prefix="/run")