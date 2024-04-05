from sqlalchemy.orm import Session
from models.database import Student, Discipline, Grade
class MockDatabase:
    def __init__(self):
        self.students = []
        self.disciplines = []
        self.grades = []
    def add_student(self, student: Student):
        self.students.append(student)
    def add_discipline(self, discipline: Discipline):
        self.disciplines.append(discipline)
    def add_grade(self, grade: Grade):
        self.grades.append(grade)
    def query_students(self):
        return self.students
    def query_disciplines(self):
        return self.disciplines
    def query_grades(self):
        return self.grades