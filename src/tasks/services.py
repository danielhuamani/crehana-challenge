from typing import List

from src.tasks.repositories import TaskRepository
from src.tasks.schemas import TaskCreateBody, TaskResponse, TaskUpdateBody


class TaskService:

    def __init__(self, repository: TaskRepository) -> None:
        self.repository: TaskRepository = repository

    def get_all(self) -> List[TaskResponse]:
        return self.repository.get_all()

    def create(self, task: TaskCreateBody) -> TaskResponse:
        return self.repository.create(task=task)

    def get_by_id(self, id: int):
        return self.repository.get_by_id(id)

    def update(self, id: int, task: TaskUpdateBody) -> TaskResponse:
        return self.repository.update(id=id, task=task)

    def delete(self, id: int) -> None:
        return self.repository.delete(id=id)
