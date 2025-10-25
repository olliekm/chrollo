from fastapi import FastAPI, APIRouter
from models import router as models_router

app = FastAPI()

v1_router = APIRouter(prefix="/v1")

@app.get("/")
async def read_root():
    return {"message": "Welcome to chrollo"}

@v1_router.get("/status")
async def read_status():
    return {"status": "API is running"}

v1_router.include_router(models_router)

app.include_router(v1_router)
