from fastapi import APIRouter
from models import HealthResponse, VersionResponse, MessageResponse

router = APIRouter()

@router.get("/health", response_model=HealthResponse)
async def health_check():
    return {"status": "ok", "service": "rollout-service"}

@router.get("/api/v1/rollout/version", response_model=VersionResponse)
async def get_version():
    return {"version": "1.0.1"}

@router.get("/api/v1/rollout/strategy", response_model=MessageResponse)
async def hello():
    return {"message": "¡Hola Mundo v1.0.1 desde Argo Rollouts!"}

