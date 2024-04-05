import unittest
from controllers.analytics_controller import AnalyticsController
from models.student import Student
from models.discipline import Discipline
class TestAnalyticsController(unittest.TestCase):
    def test_analyze_student_performance(self):
        students = [
            Student(1, "John Doe", {"Math": 90, "History": 85, "English": 92}),
            Student(2, "Jane Smith", {"Math": 78, "History": 88, "English": 95}),
        ]
        result = AnalyticsController.analyze_student_performance(students)
        self.assertEqual(result["average_grade"], 86.33)
        self.assertEqual(result["median_grade"], 88.0)
if __name__ == '__main__':
    unittest.main()