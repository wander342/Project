from models.statistics_service import StatisticsService

class AnalyticsService:
    def __init__(self, data_source, entity_factory):
        self.data_source = data_source
        self.entity_factory = entity_factory

    def analyze_student_performance(self):
        students_data = self.data_source.get_mock_students()
        student_results = [self.create_student_from_data(student_data) for student_data in students_data if student_data]
        
        # Фильтруем результаты, чтобы оставить только успешно созданных студентов
        students = [student for student, success in student_results if success]
        
        # Получаем средние оценки только для корректных студентов
        average_grades = [student.get_average_grade() for student in students]
        median_grades = [StatisticsService.calculate_median(list(student.grades.values())) for student in students]

        
        return {
            "average_grade": StatisticsService.calculate_average(average_grades),
            "median_grade": StatisticsService.calculate_average(median_grades)
        }

    def create_student_from_data(self, student_data):
        student_id = student_data.get("student_id")
        student_name = student_data.get("name")
        if not student_id or not student_name:
            print(f"Не удалось создать студента для данных: {student_data}")
            return None, False
        student = self.entity_factory.create_student(student_id, student_name)
        disciplines = student_data.get("grades", {})
        for discipline, grade in disciplines.items():
            student.add_grade(discipline, grade)
        return student, True  # Возвращаем кортеж с флагом успеха создания студента
