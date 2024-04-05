from typing import List
class StatisticsService:
    @staticmethod
    def calculate_average(data: List[float]) -> float:
        if not data:
            return 0
        return sum(data) / len(data)
    @staticmethod
    def calculate_total(data: List[float]) -> float:
        return sum(data)
    @staticmethod
    def calculate_median(data: List[float]) -> float:
        if not data:
            return 0
        sorted_data = sorted(data)
        length = len(sorted_data)
        middle = length // 2
        if length % 2 == 0:
            return (sorted_data[middle - 1] + sorted_data[middle]) / 2
        else:
            return sorted_data[middle]