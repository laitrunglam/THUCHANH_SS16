from fastapi import APIRouter,status,Depends,HTTPException
from schemas import StudentRespone
from services import get_student_by_id
from sqlalchemy.orm import Session
from database import get_db

router = APIRouter(prefix='/students',tags=['Student'])

@router.get('/{student_id}',response_model=StudentRespone,status_code=status.HTTP_200_OK)
def get_student(student_id:int, db: Session=Depends(get_db)):
    student= get_student_by_id(student_id,db)
    if student == 1:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='k tim thay id'
        )
    return student
