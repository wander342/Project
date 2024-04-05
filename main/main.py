from controllers.analytics_controller import AnalyticsController
from factories.entity_factory import ConcreteEntityFactory
from models.database_singleton import DatabaseSingleton
from presenters.analytics_presenter import AnalyticsPresenter
from services.analytics_service import AnalyticsService
from views.analytics_view import AnalyticsView
def main():
    # Инициализация базы данных
    db_singleton = DatabaseSingleton()
    db_session = db_singleton.get_session()
    # Инициализация фабрики и моделей
    entity_factory = ConcreteEntityFactory()
    analytics_service = AnalyticsService(db_session, entity_factory)
        # Инициализация представления и контроллера
    analytics_view = AnalyticsView()
    analytics_controller = AnalyticsController(analytics_service, analytics_view)
    # Анализ и отображение результатов
    analytics_controller.analyze_and_display()
if __name__ == "__main__":
    main()