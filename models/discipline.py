class Discipline:
    def __init__(self, discipline_id, name):
        self.discipline_id = discipline_id
        self.name = name
        self.students = []  # Список студентов с оценками по данной дисциплине
    def add_student(self, student, grade):
        self.students.append({"student": student, "grade": grade})
    def get_students_count(self):
        return len(self.students)