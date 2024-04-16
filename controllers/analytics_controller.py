from presenters.analytics_presenter import AnalyticsPresenter

class AnalyticsController:
    def __init__(self, analytics_service, analytics_view):
        self.analytics_service = analytics_service
        self.analytics_view = analytics_view

    def analyze_student_performance(self):
        analysis_results = self.analytics_service.analyze_student_performance()
        self.analytics_view.display_analysis_results(analysis_results)
        return analysis_results
