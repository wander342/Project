from abc import ABC, abstractmethod
from models.student import Student
from models.discipline import Discipline
class EntityFactory(ABC):
    @abstractmethod
    def create_student(self, student_id: int, name: str) -> Student:
        pass
    @abstractmethod
    def create_discipline(self, discipline_id: int, name: str) -> Discipline:
        pass
# Конкретная реализация фабрики
class ConcreteEntityFactory(EntityFactory):
    def create_student(self, student_id: int, name: str) -> Student:
        return Student(student_id, name)
    def create_discipline(self, discipline_id: int, name: str) -> Discipline:
        return Discipline(discipline_id, name)