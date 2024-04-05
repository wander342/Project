class MockDataSource:
    @staticmethod
    def get_mock_students():
        return [
            {"student_id": 1, "name": "John Doe", "grades": {"Math": 90, "History": 85, "English": 92}},
            {"student_id": 2, "name": "Jane Smith", "grades": {"Math": 78, "History": 88, "English": 95}},
        ]
    @staticmethod
    def get_mock_disciplines():
        return [
            {"discipline_id": 101, "name": "Math"},
            {"discipline_id": 102, "name": "History"},
            {"discipline_id": 103, "name": "English"},
            # Добавьте дополнительные дисциплины по аналогии
        ]