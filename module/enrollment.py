from database import Base
from sqlalchemy import Column, String,Integer,ForeignKey
from sqlalchemy.orm import relationship

class EnrollmentModule(Base):
    __tablename__ ='enrollments'
    
    id = Column(Integer,primary_key=True)
    student_id= Column(Integer,ForeignKey('students.id'),nullable= False)
    course_id = Column(Integer,ForeignKey('courses.id'),nullable= False)

    