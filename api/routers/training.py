from fastapi import APIRouter, Depends
from models.models import ModelRequest
from auth.auth_bearer import JWTBearer

router = APIRouter(prefix="/training")

@router.post("/upload", dependencies=[Depends(JWTBearer())])
async def upload_training_config(model_request: ModelRequest):
    return {"message": "Model uploaded successfully"}
