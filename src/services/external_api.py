import requests
from fastapi import HTTPException

class ExternalAPI:
    def fetch_data(self):
        try:
            response = requests.get("https://jsonplaceholder.typicode.com/todos/1", timeout=5)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise HTTPException(status_code=503, detail=f"Fallo en la API externa: {str(e)}")
