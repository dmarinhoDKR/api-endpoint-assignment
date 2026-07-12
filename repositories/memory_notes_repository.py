from repositories.notes_repository import Note, NotesRepository


class MemoryNotesRepository(NotesRepository):
    def __init__(self):
        self.notes: list[Note] = []

    def create(self, title: str, content: str) -> Note:
        new_note: Note = {
            "id": len(self.notes) + 1,
            "title": title,
            "content": content,
        }

        self.notes.append(new_note)
        return new_note

    def list_all(self) -> list[Note]:
        return self.notes
