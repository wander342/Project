from abc import ABC, abstractmethod
from typing import List

# Пример класса Student и Grade для полноты контекста
class Student:
    def __init__(self, name):
        self.name = name

class Grade:
    def __init__(self, student, grade):
        self.student = student
        self.grade = grade

class AnalyticsObserver(ABC):
    @abstractmethod
    def update(self, students: List['Student'], grades: List['Grade']):
        pass

# Конкретный класс-наблюдатель
class GradeAnalyticsObserver(AnalyticsObserver):
    def update(self, students: List['Student'], grades: List['Grade']):
        # Реализация обновления аналитики успеваемости по оценкам
        total_students = len(students)
        total_grades = len(grades)
        average_grade = sum(grade.grade for grade in grades) / total_grades if total_grades > 0 else 0
        print(f"Total students: {total_students}, Total grades: {total_grades}, Average grade: {average_grade}")

# Пример использования
if __name__ == "__main__":
    students = [Student("Alice"), Student("Bob"), Student("Charlie")]
    grades = [Grade(students[0], 90), Grade(students[1], 85), Grade(students[2], 95)]

    observer = GradeAnalyticsObserver()
    observer.update(students, grades)
