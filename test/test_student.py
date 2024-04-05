import unittest
from models.student import Student
class TestStudent(unittest.TestCase):
    def test_add_grade(self):
        student = Student(1, "John Doe")
        student.add_grade("Math", 90)
        self.assertEqual(student.disciplines["Math"], 90)
    def test_get_average_grade(self):
        student = Student(1, "John Doe", {"Math": 90, "History": 85, "English": 92})
        result = student.get_average_grade()
        self.assertEqual(result, 89.0)
if __name__ == '__main__':
    unittest.main()