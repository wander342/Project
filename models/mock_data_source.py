class MockDataSource:
    def __init__(self):
        self.students = []

    def get_mock_students(self):
        return self.students

    def add_student(self, student_data):
        self.students.append(student_data)

    @staticmethod
    def get_mock_students():
        return [
            {"student_id": 1, "name": "John Doe", "grades": {"Math": 90, "History": 85, "English": 92}},
            {"student_id": 2, "name": "Jane Smith", "grades": {"Math": 73, "History": 88, "English": 95}},
            {"student_id": 3, "name": "Orlando Doqwee", "grades": {"Math": 60, "History": 75, "English": 68}},
            {"student_id": 4, "name": "Ann Smith", "grades": {"Math": 99, "History": 64, "English": 76}},
            # Добавьте дополнительных студентов с оценками по аналогии
        ]
