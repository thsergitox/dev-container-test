import requests
import asyncio

import logging

# Configuración básica de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class APIClient:
    def __init__(self, base_url, session=None):
        self.base_url = base_url
        # Inyección de dependencias: permitimos inyectar una sesión personalizada
        self.session = session or requests.Session()

    def get_todo(self, todo_id):
        logger.info(f"Obteniendo todo con ID {todo_id}")
        try:
            response = self.session.get(f"{self.base_url}/todos/{todo_id}")
            response.raise_for_status()
            logger.info(f"Todo obtenido: {response.json()}")
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            logger.error(f"Error HTTP: {http_err}")
            raise Exception(f"HTTP error occurred: {http_err}") from http_err
        except Exception as err:
            logger.error(f"Error desconocido: {err}")
            raise Exception(f"An error occurred: {err}") from err

    def create_todo(self, data):
        response = self.session.post(f"{self.base_url}/todos", json=data)
        response.raise_for_status()
        return response.json()

    def update_todo(self, todo_id, data):
        response = self.session.put(f"{self.base_url}/todos/{todo_id}", json=data)
        response.raise_for_status()
        return response.json()

    def delete_todo(self, todo_id):
        response = self.session.delete(f"{self.base_url}/todos/{todo_id}")
        response.raise_for_status()
        return response.status_code == 200

    async def async_get_todo(self, todo_id):
        loop = asyncio.get_event_loop()
        response = await loop.run_in_executor(None, self.session.get, f"{self.base_url}/todos/{todo_id}")
        response.raise_for_status()
        return response.json()