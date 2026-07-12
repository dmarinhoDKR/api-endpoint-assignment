from repositories.memory_notes_repository import MemoryNotesRepository
from services.notes_service import NotesService

notes_repository = MemoryNotesRepository()
notes_service = NotesService(notes_repository)
