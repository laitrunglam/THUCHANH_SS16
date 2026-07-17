from pydantic import BaseModel

class EnrollmentCreate(BaseModel):
    student_id: int
    course_id: int


class EnrollmentRespone(EnrollmentCreate):
    id: int 