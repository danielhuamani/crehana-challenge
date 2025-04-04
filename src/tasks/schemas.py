from pydantic import BaseModel


class TaskBase(BaseModel):
    title: str
    description: str


class TaskCreateBody(TaskBase):
    ...


class TaskUpdateBody(TaskBase):
    completed: bool


class TaskResponse(TaskBase):
    id: int
    completed: bool


class TaskMessageResponse(BaseModel):
    message: str