from fastapi import APIRouter

router = APIRouter(prefix="/models")

@router.post("/upload")
async def upload_model():
    return {"message": "Model uploaded successfully"}
