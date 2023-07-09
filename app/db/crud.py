from sqlalchemy.orm import Session

from app.schemas.todos import CreateTodo, UpdateTodo
from app.db import models

from sqlalchemy import delete


class TodoNotFound(Exception):
    pass


def get_todo(db: Session, todo_id: int):
    return db.query(models.Todo).filter(models.Todo.id == todo_id).first()


def get_todos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Todo).offset(skip).limit(limit).all()


def create_todo(db: Session, todo: CreateTodo):
    db_todo = models.Todo(**todo.model_dump())
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo


def update_todo(db: Session, id: int, todo: UpdateTodo):
    db_todo = db.query(models.Todo).get(id)
    if not db_todo:
        raise TodoNotFound
    db_todo.completed = todo.completed
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo


def delete_todo(db: Session, id: int):
    db_todo = db.query(models.Todo).get(id)
    if not db_todo:
        raise TodoNotFound
    db.delete(db_todo)
    db.commit()


def delete_completed_todo(db: Session):
    statement = delete(models.Todo).where(models.Todo.completed == True)
    db.execute(statement)
    db.commit()