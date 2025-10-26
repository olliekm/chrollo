from fastapi import APIRouter
from models.models import ModelRequest

router = APIRouter(prefix="/training")

@router.post("/upload")
async def upload_training_config(model_request: ModelRequest):
    return {"message": "Model uploaded successfully"}
