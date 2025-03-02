import sys
import os

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
from core.logging_config import setup_logging
from api.routes import router

# Configurar logs
logger = setup_logging()

# Inicializar FastAPI
app = FastAPI(title="Rollout Service", version="1.0.3")

# Instrumentar Prometheus
Instrumentator().instrument(app).expose(app)

# Incluir rutas
app.include_router(router)

# Middleware de error global
@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    logger.error(f"Error: {exc}")
    return {"message": "Internal Server Error"}
