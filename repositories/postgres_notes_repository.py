import psycopg

from repositories.notes_repository import Note, NotesRepository


class PostgresNotesRepository(NotesRepository):
    def __init__(self, database_url: str):
        self.database_url = database_url

    def create(self, title: str, content: str) -> Note:
        with psycopg.connect(self.database_url) as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    """
                    INSERT INTO notes (title, content)
                    VALUES (%s, %s)
                    RETURNING id, title, content
                    """,
                    (title, content),
                )
                row = cursor.fetchone()

        if row is None:
            raise RuntimeError("The database did not return the created note.")

        return {
            "id": row[0],
            "title": row[1],
            "content": row[2],
        }

    def list_all(self) -> list[Note]:
        with psycopg.connect(self.database_url) as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT id, title, content
                    FROM notes
                    ORDER BY id
                    """
                )
                rows = cursor.fetchall()

        return [
            {
                "id": row[0],
                "title": row[1],
                "content": row[2],
            }
            for row in rows
        ]
