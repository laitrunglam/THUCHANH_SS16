from sqlalchemy.orm import Session
from module import StudentModel

def get_student_by_id(student_id: int, db: Session):
    student= db.query(StudentModel).filter(student_id== StudentModel.id).first()
    if not student:
        return 1
    return {
        'id': student.id,
        'full_name': student.full_name,
        'status': student.status,
        'department': student.department,
        'course': student.courses
    }