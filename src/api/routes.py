from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from services.business_logic import process_data
from repositories.database import save_data, get_data
from models.schemas import MessageResponse, VersionResponse, HealthResponse
import datetime

router = APIRouter()

class StoreDataRequest(BaseModel):
    key: int
    value: str

@router.get("/health", response_model=HealthResponse)
async def health_check():
    return {"status": "ok", "service": "rollout-service"}

@router.get("/api/v1/rollout/version", response_model=VersionResponse)
async def get_version():
    return {"version": "1.0.2"}

@router.get("/api/v1/rollout/strategy", response_model=MessageResponse)
async def hello():
    return {"message": "¡Hola Mundo v1.0.13 desde Argo Rollouts!"}

@router.get("/api/v1/rollout/external")
async def fetch_external_data():
    try:
        return process_data()
    except Exception as e:
        raise HTTPException(
            status_code=503,
            detail={
                "error": "Fallo en la API externa",
                "status_code": 503,
                "timestamp": datetime.datetime.utcnow().isoformat(),
                "message": str(e),
            }
        )

@router.post("/api/v1/rollout/store")
async def store_data(request: StoreDataRequest):
    if request.key < 0:
        raise HTTPException(
            status_code=400,
            detail={
                "error": "El key debe ser un número positivo.",
                "status_code": 400,
                "timestamp": datetime.datetime.utcnow().isoformat(),
            }
        )
    return {"saved": save_data(request.key, request.value)}

@router.get("/api/v1/rollout/store/{key}")
async def retrieve_data(key: int):
    value = get_data(key)
    if value is None:
        raise HTTPException(
            status_code=404,
            detail={
                "error": "Dato no encontrado.",
                "status_code": 404,
                "timestamp": datetime.datetime.utcnow().isoformat(),
            }
        )
    return {"value": value}
