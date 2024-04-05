import unittest
from factories.entity_factory import EntityFactory
class TestEntityFactory(unittest.TestCase):
    def test_create_student(self):
        factory = EntityFactory()
        student = factory.create_student(1, "John Doe")
        self.assertEqual(student.student_id, 1)
        self.assertEqual(student.name, "John Doe")
    def test_create_discipline(self):
        factory = EntityFactory()
        discipline = factory.create_discipline(101, "Math")
        self.assertEqual(discipline.discipline_id, 101)
        self.assertEqual(discipline.name, "Math")
if __name__ == '__main__':
    unittest.main()