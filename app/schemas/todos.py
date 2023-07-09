from pydantic import BaseModel


class BaseTodo(BaseModel):
    text: str
    completed: bool = False


class Todo(BaseTodo):
    id: int

    class Config:
        orm_mode = True


class CreateTodo(BaseTodo):
    pass


class UpdateTodo(BaseModel):
    completed: bool