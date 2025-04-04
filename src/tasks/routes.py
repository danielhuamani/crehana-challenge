from typing import Union, List

from fastapi import FastAPI, status, APIRouter, Request, HTTPException
from src.core.session import SessionDep
from src.tasks.schemas import TaskCreateBody, TaskResponse, TaskUpdateBody, TaskMessageResponse
from src.tasks.services import TaskService
from src.tasks.repositories import TaskRepository
from src.tasks.exceptions import NotFoundException

router = APIRouter()

@router.get("/tasks", response_model=List[TaskResponse], status_code=status.HTTP_200_OK)
def tasks(session: SessionDep):
    repository = TaskRepository(session=session)
    response: List[TaskResponse] = TaskService(repository=repository).get_all()
    return response

@router.post("/tasks", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def tasks(session: SessionDep, task: TaskCreateBody):
    repository = TaskRepository(session=session)
    response: TaskResponse = TaskService(repository=repository).create(task)
    return response


@router.get("/tasks/{id}", response_model=TaskResponse, status_code=status.HTTP_200_OK)
def tasks(session: SessionDep, id: int):
    repository = TaskRepository(session=session)
    try:
        response: TaskResponse = TaskService(repository=repository).get_by_id(id)
    except NotFoundException as not_found_exception:
        raise HTTPException(
            status_code=not_found_exception.status_code,
            detail=not_found_exception.message
        )
    return response

@router.put("/tasks/{id}", response_model=TaskResponse, status_code=status.HTTP_200_OK)
def tasks(session: SessionDep, id: int, task: TaskUpdateBody):
    repository = TaskRepository(session=session)
    try:
        response: TaskResponse = TaskService(repository=repository).update(
            id=id,
            task=task
        )
    except NotFoundException as not_found_exception:
        raise HTTPException(
            status_code=not_found_exception.status_code,
            detail=not_found_exception.message
        )
    return response


@router.delete("/tasks/{id}", status_code=status.HTTP_200_OK)
def tasks(session: SessionDep, id: int):
    repository = TaskRepository(session=session)
    try:
        TaskService(repository=repository).delete(
            id=id
        )
    except NotFoundException as not_found_exception:
        raise HTTPException(
            status_code=not_found_exception.status_code,
            detail=not_found_exception.message
        )
    return TaskMessageResponse(message="Task deleted")
