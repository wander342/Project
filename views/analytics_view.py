class ConsoleView:
    @staticmethod
    def display_analysis_results(analysis_results):
        print("Анализ успеваемости студентов:")
        print(f"Средний балл по всем студентам: {analysis_results['average_grade']:.2f}")
        print(f"Медианный балл по всем студентам: {analysis_results['median_grade']:.2f}")