class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.grades = {}  # Словарь для хранения оценок по каждой дисциплине

    def add_grade(self, discipline, grade):
        self.grades[discipline] = grade
        
    def get_grades(self):
        return self.grades
    
    def get_average_grade(self):
        if not self.grades:
            return 0
        return sum(self.grades.values()) / len(self.grades)
