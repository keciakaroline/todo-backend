from fastapi import FastAPI

from app.db import models
from app.db.database import engine
from app.routes.todos import todos_router

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router=todos_router, prefix="/todos")
