class MockDatabase:
    def __init__(self):
        self.students = []
        self.disciplines = []
        self.grades = []

    def add_student(self, student):
        self.students.append(student)

    def add_discipline(self, discipline):
        self.disciplines.append(discipline)

    def add_grade(self, grade):
        self.grades.append(grade)

    def query_students(self):
        return self.students

    def query_disciplines(self):
        return self.disciplines

    def query_grades(self):
        return self.grades
