from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, Session
Base = declarative_base()
class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, unique=True, index=True)
    name = Column(String)
    grades = relationship('Grade', back_populates='student')
class Discipline(Base):
    __tablename__ = 'disciplines'
    id = Column(Integer, primary_key=True, index=True)
    discipline_id = Column(Integer, unique=True, index=True)
    name = Column(String)
    students = relationship('Grade', back_populates='discipline')
class Grade(Base):
    __tablename__ = 'grades'
    id = Column(Integer, primary_key=True, index=True)
    value = Column(Integer)
    student_id = Column(Integer, ForeignKey('students.id'))
    discipline_id = Column(Integer, ForeignKey('disciplines.id'))
# Создаем базу данных
DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(bind=engine)