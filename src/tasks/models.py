from sqlmodel import Field, SQLModel


class Task(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    title: str = Field(max_length=255)
    description: str = Field(max_length=255)
    completed: bool = False
