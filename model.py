from pydantic import BaseModel

# Course 리스트 형식
class Course(BaseModel):
    course_name: str
    year: int
    semester: int
    grade: str