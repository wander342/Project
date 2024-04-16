from flask import Flask, render_template
from controllers.analytics_controller import AnalyticsController
from presenters.analytics_presenter import AnalyticsPresenter
from services.analytics_service import AnalyticsService
from models.mock_data_source import MockDataSource
from factories.entity_factory import ConcreteEntityFactory

app = Flask(__name__)

@app.route('/')
def index():
    mock_data_source = MockDataSource()
    entity_factory = ConcreteEntityFactory()
    analytics_service = AnalyticsService(mock_data_source, entity_factory)
    analytics_controller = AnalyticsController(analytics_service, AnalyticsPresenter())
    analysis_results = analytics_controller.analyze_student_performance()
    return render_template('index.html', analysis_results=analysis_results)

if __name__ == '__main__':
    app.run(debug=True)
