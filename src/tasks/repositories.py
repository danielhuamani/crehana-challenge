from typing import List

from sqlmodel import select

from src.core.session import SessionDep
from src.tasks.exceptions import NotFoundException
from src.tasks.models import Task
from src.tasks.schemas import TaskCreateBody, TaskResponse, TaskUpdateBody


class TaskRepository:

    def __init__(self, session: SessionDep) -> None:
        self.session: SessionDep = session

    def get_all(self) -> List[TaskResponse]:
        db_tasks = self.session.exec(select(Task)).all()
        return [
            TaskResponse.model_validate(db_task.model_dump()) for db_task in db_tasks
        ]

    def create(self, task: TaskCreateBody) -> TaskResponse:
        db_task = Task.model_validate(task, update={"completed": False})
        self.session.add(db_task)
        self.session.commit()
        self.session.refresh(db_task)
        return TaskResponse.model_validate(db_task.model_dump())

    def _get_by_id(self, id: int) -> Task:
        statement = select(Task).where(Task.id == id)
        db_task = self.session.exec(statement).first()
        if not db_task:
            raise NotFoundException(message=f"Task with id {id} not found")
        return db_task

    def get_by_id(self, id: int) -> TaskResponse:
        db_task = self._get_by_id(id)
        return TaskResponse.model_validate(db_task.model_dump())

    def update(self, id: int, task: TaskUpdateBody) -> TaskResponse:
        db_task: Task = self._get_by_id(id=id)
        task_data = task.model_dump()
        db_task.sqlmodel_update(task_data)
        self.session.add(db_task)
        self.session.commit()
        self.session.refresh(db_task)
        return TaskResponse.model_validate(db_task.model_dump())

    def delete(self, id: int) -> None:
        db_task: Task = self._get_by_id(id=id)
        self.session.delete(db_task)
        self.session.commit()
        return None
