from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Grade(Base):
    __tablename__ = 'grades'
    id = Column(Integer, primary_key=True, index=True)
    value = Column(Integer)
    student_id = Column(Integer, ForeignKey('students.id'))
    discipline_id = Column(Integer, ForeignKey('disciplines.id'))

    student = relationship("Student", back_populates="grades")
    discipline = relationship("Discipline", back_populates="grades")
