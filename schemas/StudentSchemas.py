from pydantic import BaseModel, ConfigDict
from .departmentSchemas import DepartmentCreate
from .courseSchemas import CourseRespone

class StudentRespone(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    full_name: str
    status: str
    department: DepartmentCreate
    courses: list[CourseRespone]