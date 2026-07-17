from database import Base
from sqlalchemy import Column, String,Integer
from sqlalchemy.orm import relationship

class DepartmentModel(Base):
    __tablename__ = 'departments'

    id = Column(Integer,primary_key= True)
    name = Column(String(50))

    students = relationship('StudentModel', back_populates='department' )