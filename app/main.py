from fastapi import FastAPI, HTTPException, Request
from prometheus_fastapi_instrumentator import Instrumentator
from logging_config import setup_logging
from routes import router

# Configurar logs
logger = setup_logging()

# Inicializar FastAPI
app = FastAPI(title="Rollout Service", version="1.0.1")

# Instrumentar Prometheus
Instrumentator().instrument(app).expose(app)

# Incluir rutas
app.include_router(router)

# Middleware para capturar errores y devolver respuestas JSON
@app.exception_handler(Exception)
async def generic_exception_handler(request: Request, exc: Exception):
    logger.error(f"Error no manejado: {exc}")
    return JSONResponse(
        status_code=500,
        content={"message": "Internal Server Error"}
    )

