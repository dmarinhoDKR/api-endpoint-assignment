from abc import ABC, abstractmethod

Note = dict[str, int | str]


class NotesRepository(ABC):
    @abstractmethod
    def create(self, title: str, content: str) -> Note:
        pass

    @abstractmethod
    def list_all(self) -> list[Note]:
        pass
