from fastapi import APIRouter
from pydantic import BaseModel
from services.business_logic import process_data
from repositories.database import save_data, get_data
from models.schemas import MessageResponse, VersionResponse, HealthResponse

router = APIRouter()

class StoreDataRequest(BaseModel):
    key: int
    value: str

@router.get("/health", response_model=HealthResponse)
async def health_check():
    return {"status": "ok", "service": "rollout-service"}


@router.get("/api/v1/rollout/version", response_model=VersionResponse)
async def get_version():
    return {"version": "1.0.3"}


@router.get("/api/v1/rollout/strategy", response_model=MessageResponse)
async def hello():
    return {"message": "¡Hola Mundo v1.0.3 desde Argo Rollouts!"}


@router.get("/api/v1/rollout/external")
async def fetch_external_data():
    return process_data()


@router.post("/api/v1/rollout/store")
async def store_data(request: StoreDataRequest):
    return {"saved": save_data(request.key, request.value)}


@router.get("/api/v1/rollout/store/{key}")
async def retrieve_data(key: int):
    return {"value": get_data(key)}
