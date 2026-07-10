from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="API Endpoint Assignment")

class NoteCreate(BaseModel):
    title: str
    content: str


notes = []


@app.get("/")
def root():
    return {
        "message": "Hello from my backend API Assignment",
        "status": "running",
    }


@app.get("/profile")
def profile():
    return {
        "name": "Daniel Figueiredo",
        "track": "Backend AI Engineering",
        "focus": ["Python", "APIs", "Automation", "MLOps"],
    }


@app.post("/notes")
def create_note(note: NoteCreate):
    new_note = {
        "id": len(notes) + 1,
        "title": note.title,
        "content": note.content,
    }

    notes.append(new_note)

    return new_note


@app.get("/notes")
def list_notes():
    return notes
