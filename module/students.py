from database import Base
from sqlalchemy import Column, String,Integer,ForeignKey
from sqlalchemy.orm import relationship

class StudentModel(Base):
    __tablename__ = 'students'

    id= Column(Integer,primary_key= True)
    full_name=Column(String(50),nullable= False)
    status = Column(String(50),default= 'ACTIVE',nullable= False)
    department_id= Column(String(50), ForeignKey('departments.id'))
    

    department = relationship('DepartmentModel', back_populates='students')

    courses = relationship(
        'CousreModule',
        secondary='enrollments',
        back_populates='students'
    )



    

