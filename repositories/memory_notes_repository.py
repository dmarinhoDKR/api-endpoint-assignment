class MemoryNotesRepository:
    def __init__(self):
        self.notes = []

    def create(self, title: str, content: str):
        new_note = {
            "id": len(self.notes) + 1,
            "title": title,
            "content": content,
        }

        self.notes.append(new_note)
        return new_note
    
    def list_all(self):
        return self.notes