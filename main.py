from fastapi import FastAPI
from pydantic import BaseModel

from dependencies import notes_service

app = FastAPI(title="API Endpoint Assignment")


class NoteCreate(BaseModel):
    title: str
    content: str


@app.get("/")
def root():
    return {
        "message": "Hello from my backend API Assignment",
        "status": "running",
    }


@app.get("/profile")
def profile():
    return {
        "name": "Daniel Figueredo",
        "track": "Backend AI Engineering",
        "focus": ["Python", "APIs", "Automation", "MLOps"],
    }


@app.post("/notes")
def create_note(note: NoteCreate):
    return notes_service.create_note(
        title=note.title,
        content=note.content,
    )


@app.get("/notes")
def list_notes():
    return notes_service.list_notes()
