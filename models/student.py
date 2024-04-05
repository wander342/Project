class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.disciplines = {}  # Словарь для хранения дисциплин и оценок
    def add_grade(self, discipline, grade):
        self.disciplines[discipline] = grade
    def get_average_grade(self):
        if not self.disciplines:
            return 0
        return sum(self.disciplines.values()) / len(self.disciplines)

