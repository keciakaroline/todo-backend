from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db import crud
from app.db.crud import TodoNotFound
from app.db.database import get_db
from app.schemas.todos import CreateTodo, UpdateTodo, Todo

todos_router = APIRouter()


@todos_router.post("/", response_model=Todo)
async def create_todos(todo: CreateTodo, db: Session = Depends(get_db)):
    return crud.create_todo(db=db, todo=todo)


@todos_router.get("/", response_model=List[Todo])
async def read_todos(db: Session = Depends(get_db)):
    return crud.get_todos(db)


@todos_router.put("/{id}", response_model=Todo)
async def update_todos(id: int, todo: UpdateTodo, db: Session = Depends(get_db)):
    return crud.update_todo(db, id, todo)


@todos_router.delete("/{id}")
async def delete_todos(id: int, db: Session = Depends(get_db)):
    try:
        crud.delete_todo(db, id)
        return True
    except TodoNotFound:
        raise HTTPException(status_code=404, detail=f"todo {id} not found")
    except Exception:
        raise HTTPException(status_code=400, detail="Cannot delete todo")

@todos_router.delete("/completed")
async def delete_completed_todos(db: Session = Depends(get_db)):
    try:
        crud.delete_completed_todo(db)
        return True
    except Exception:
        raise HTTPException(status_code=400, detail="Cannot delete todo")
