import requests
from fastapi import HTTPException
import pybreaker
from timeit import default_timer as timer
from core.metrics import EXTERNAL_API_CALLS_TOTAL, EXTERNAL_API_CALL_DURATION_SECONDS
from core.config import settings
external_api_breaker = pybreaker.CircuitBreaker(fail_max=3, reset_timeout=10, exclude=[HTTPException])


class ExternalAPI:
    @external_api_breaker
    def fetch_data(self):
        start_time = timer()
        try:
            response = requests.get(settings.EXTERNAL_API_URL, timeout=5)
            response.raise_for_status() 
            EXTERNAL_API_CALLS_TOTAL.labels(status='success').inc()
            end_time = timer()
            duration = end_time - start_time
            EXTERNAL_API_CALL_DURATION_SECONDS.labels(status='success').observe(duration)
            return response.json()

        except requests.exceptions.RequestException as e:
            EXTERNAL_API_CALLS_TOTAL.labels(status='failure').inc()
            end_time = timer()
            duration = end_time - start_time
            EXTERNAL_API_CALL_DURATION_SECONDS.labels(status='failure').observe(duration)
            raise HTTPException(status_code=503, detail=f"Fallo en la API externa: {str(e)}")
