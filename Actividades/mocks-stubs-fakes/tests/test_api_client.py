import pytest
from src.api_client import APIClient
import asyncio

# Usaremos requests-mock para facilitar el mocking de requests
import requests
import requests_mock

# Mock: Simulamos el comportamiento de una dependencia externa
def test_get_todo_successful_response():
    with requests_mock.Mocker() as m:
        m.get("https://example.com/todos/1", json={"id": 1, "title": "Test Todo", "completed": False}, status_code=200)
        client = APIClient("https://example.com")
        todo = client.get_todo(1)
        assert todo["title"] == "Test Todo"

# Stub: Simulamos una respuesta predefinida, sin lógica compleja
class FakeSession:
    def get(self, url):
        class Response:
            status_code = 200
            def json(self):
                return {"id": 1, "title": "Test Todo", "completed": False}
            def raise_for_status(self):
                pass
        return Response()

def test_get_todo_with_fake_session():
    fake_session = FakeSession()
    client = APIClient("https://example.com", session=fake_session)
    todo = client.get_todo(1)
    assert todo["title"] == "Test Todo"

# Spy: Verificamos que ciertos métodos fueron llamados
def test_get_todo_calls_get_method(mocker):
    mock_session = mocker.Mock()
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"id": 1, "title": "Test Todo", "completed": False}
    mock_session.get.return_value = mock_response

    client = APIClient("https://example.com", session=mock_session)
    todo = client.get_todo(1)

    mock_session.get.assert_called_once_with("https://example.com/todos/1")
    assert todo["title"] == "Test Todo"

# Fake: Usamos una implementación simple que funciona para pruebas
class FakeRequestsSession(requests.Session):
    def get(self, url, **kwargs):
        response = requests.Response()
        response.status_code = 200
        response._content = b'{"id": 1, "title": "Test Todo", "completed": false}'
        return response

# Mock: Simulamos el comportamiento de una dependencia externa para create_todo
def test_create_todo_successful_response():
    with requests_mock.Mocker() as m:
        m.post("https://example.com/todos", json={"id": 1, "title": "New Todo", "completed": False}, status_code=201)
        client = APIClient("https://example.com")
        new_todo = {"title": "New Todo", "completed": False}
        created_todo = client.create_todo(new_todo)
        assert created_todo["title"] == "New Todo"
        assert created_todo["completed"] is False

def test_get_todo_with_fake_requests_session():
    fake_session = FakeRequestsSession()
    client = APIClient("https://example.com", session=fake_session)
    todo = client.get_todo(1)
    assert todo["title"] == "Test Todo"

# Prueba de integración: Realizamos una llamada real a la API REST
def test_get_todo_integration():
    client = APIClient("https://jsonplaceholder.typicode.com")
    todo = client.get_todo(1)
    assert todo["id"] == 1

def test_get_todo_performance(benchmark, mocker):
    mock_session = mocker.Mock()
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "id": 1,
        "title": "Test Todo",
        "completed": False
    }
    mock_session.get.return_value = mock_response

    client = APIClient("https://example.com", session=mock_session)

    def fetch_todo():
        client.get_todo(1)

    result = benchmark(fetch_todo)
    assert result is None  # La función no retorna nada

@pytest.mark.asyncio
async def test_async_get_todo(mocker):
    mock_session = mocker.Mock()
    mock_response = mocker.Mock()
    mock_response.raise_for_status.return_value = None
    mock_response.json.return_value = {
        "id": 1,
        "title": "Async Todo",
        "completed": False
    }
    mock_session.get.return_value = mock_response

    client = APIClient("https://example.com", session=mock_session)
    todo = await client.async_get_todo(1)
    assert todo["title"] == "Async Todo"