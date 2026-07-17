from database import Base
from sqlalchemy import Column, String,Integer
from sqlalchemy.orm import relationship

class CousreModule(Base):
    __tablename__ = 'courses'

    id=Column(Integer,primary_key= True)
    name= Column(String(50),nullable= False)
    status= Column(String(50),default='OPEN')

    students = relationship(
        'StudentModel',
        secondary= 'enrollments',
        back_populates= 'courses'
    )
    