import os

from repositories.postgres_notes_repository import PostgresNotesRepository
from services.notes_service import NotesService

database_url = os.environ["DATABASE_URL"]

notes_repository = PostgresNotesRepository(database_url)
notes_service = NotesService(notes_repository)
