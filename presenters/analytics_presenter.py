class AnalyticsPresenter:
    @staticmethod
    def display_analysis_results(analysis_results):
        print("Student Performance Analysis:")
        print(f"Average Grade: {analysis_results['average_grade']:.2f}")
        print(f"Median Grade: {analysis_results['median_grade']:.2f}")
