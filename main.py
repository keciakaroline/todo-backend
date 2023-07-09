from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.db import models
from app.db.database import engine
from app.routes.todos import todos_router

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router=todos_router, prefix="/todos")
