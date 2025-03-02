import requests

class ExternalAPI:
    def fetch_data(self):
        response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
        return response.json()