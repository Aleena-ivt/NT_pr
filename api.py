from fastapi import FastAPI
from todo import todo_router
from model import Todo


app = FastAPI(
    title="Todo API_Петрова А.А., ИВТ-ИСОИ-401Б"
)

app.include_router(todo_router)
