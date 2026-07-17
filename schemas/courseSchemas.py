from pydantic import BaseModel, ConfigDict

class CourseRespone(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    status : str