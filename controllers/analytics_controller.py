from models.statistics_service import StatisticsService
class AnalyticsController:
    @staticmethod
    def analyze_student_performance(students):
        average_grades = [student.get_average_grade() for student in students]
        median_grades = [StatisticsService.calculate_median(list(student.disciplines.values())) for student in students]
        return {
            "average_grade": StatisticsService.calculate_average(average_grades),
            "median_grade": StatisticsService.calculate_average(median_grades)
        }