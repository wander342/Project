import unittest
from models.statistics_service import StatisticsService
class TestStatisticsService(unittest.TestCase):
    def test_calculate_average(self):
        data = [10, 20, 30, 40, 50]
        result = StatisticsService.calculate_average(data)
        self.assertEqual(result, 30.0)
    def test_calculate_average_empty_data(self):
        data = []
        result = StatisticsService.calculate_average(data)
        self.assertEqual(result, 0)
    def test_calculate_median_odd_length(self):
        data = [3, 1, 4, 1, 5]
        result = StatisticsService.calculate_median(data)
        self.assertEqual(result, 3)
    def test_calculate_median_even_length(self):
        data = [7, 2, 8, 1]
        result = StatisticsService.calculate_median(data)
        self.assertEqual(result, 4.5)
    def test_calculate_median_empty_data(self):
        data = []
        result = StatisticsService.calculate_median(data)
        self.assertEqual(result, 0)
if __name__ == '__main__':
    unittest.main()