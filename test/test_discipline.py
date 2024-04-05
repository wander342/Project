import unittest
from models.discipline import Discipline
class TestDiscipline(unittest.TestCase):
    def test_add_student(self):
        discipline = Discipline(101, "Math")
        discipline.add_student("John Doe")
        self.assertEqual(discipline.students, ["John Doe"])
    def test_get_students_count(self):
        discipline = Discipline(101, "Math")
        discipline.students = ["John Doe", "Jane Smith", "Bob Johnson"]
        result = discipline.get_students_count()
        self.assertEqual(result, 3)
if __name__ == '__main__':
    unittest.main()