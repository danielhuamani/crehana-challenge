from fastapi.testclient import TestClient
from fastapi import status
from sqlmodel import Session
from src.tasks.exceptions import NotFoundException
from src.tasks.repositories import TaskRepository
from src.tasks.schemas import (TaskCreateBody, TaskMessageResponse,
                               TaskResponse, TaskUpdateBody)
from src.tasks.services import TaskService

def test_create_task(
    client: TestClient
) -> None:
    data = {"title": "Prueba 123", "description": "Description prueba 123"}
    response = client.post("/tasks/",
        json=data,
    )
    response_json = response.json()
    assert response.status_code == status.HTTP_201_CREATED
    assert response_json["title"] == data["title"]
    assert response_json["description"] == data["description"]
    assert "id" in response_json

def test_read_tasks(
    client: TestClient,
    db: Session
) -> None:
    task_body = TaskCreateBody(title="prueba test", description="description test")
    repository = TaskRepository(session=db)
    task_response: TaskResponse = TaskService(repository=repository).create(task_body)
    response = client.get("/tasks/")
    response_json = response.json()
    assert response.status_code == status.HTTP_200_OK
    assert len(response_json) == 1
    assert response_json[0]["title"] == task_response.title
    assert response_json[0]["description"] == task_response.description

def test_updated_task(
    client: TestClient,
    db: Session
) -> None:
    task_body = TaskCreateBody(title="prueba test", description="description test")
    repository = TaskRepository(session=db)
    task_response: TaskResponse = TaskService(repository=repository).create(task_body)
    data = {"title": "Prueba 123", "description": "Description prueba 123", "completed": True}
    response = client.put(f"/tasks/{task_response.id}", 
        json=data
    )
    response_json = response.json()
    assert response.status_code == status.HTTP_200_OK
    assert response_json["title"] == data["title"]
    assert response_json["description"] == data["description"]
    assert response_json["completed"] == True

def test_delete_task(
    client: TestClient,
    db: Session
) -> None:
    task_body = TaskCreateBody(title="prueba test", description="description test")
    repository = TaskRepository(session=db)
    task_response: TaskResponse = TaskService(repository=repository).create(task_body)
    data = {"title": "Prueba 123", "description": "Description prueba 123", "completed": True}
    response = client.delete(f"/tasks/{task_response.id}")
    response_json = response.json()
    assert response.status_code == status.HTTP_200_OK
    assert response_json["message"] == "Task deleted"

def test_read_task(
    client: TestClient,
    db: Session
) -> None:
    task_body = TaskCreateBody(title="prueba test", description="description test")
    repository = TaskRepository(session=db)
    task_response: TaskResponse = TaskService(repository=repository).create(task_body)
    response = client.get(f"/tasks/{task_response.id}")
    response_json = response.json()
    assert response.status_code == status.HTTP_200_OK
    assert response_json["title"] == task_response.title
    assert response_json["description"] == task_response.description

def test_read_task_not_found(
    client: TestClient,
    db: Session
) -> None:
    task_body = TaskCreateBody(title="prueba test", description="description test")
    repository = TaskRepository(session=db)
    task_response: TaskResponse = TaskService(repository=repository).create(task_body)
    response = client.get("/tasks/122222")
    response_json = response.json()
    assert response.status_code == status.HTTP_404_NOT_FOUND