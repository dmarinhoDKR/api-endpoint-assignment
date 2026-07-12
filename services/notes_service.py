from repositories.notes_repository import Note, NotesRepository


class NotesService:
    def __init__(self, repository: NotesRepository):
        self.repository = repository

    def create_note(self, title: str, content: str) -> Note:
        return self.repository.create(title, content)

    def list_notes(self) -> list[Note]:
        return self.repository.list_all()
