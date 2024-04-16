from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DatabaseSingleton:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(DatabaseSingleton, cls).__new__(cls)
            DATABASE_URL = "sqlite:///./test.db"
            cls._instance.engine = create_engine(DATABASE_URL)
            cls._instance.Session = sessionmaker(autocommit=False, autoflush=False, bind=cls._instance.engine)
        return cls._instance

    def get_session(self):
        return self.Session()
