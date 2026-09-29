from fastapi import APIRouter
from pydantic import BaseModel
from routers import course_db as db
router = APIRouter(prefix="/courses", tags=["Courses"])

class Course(BaseModel):
    name:str
    duration:int
    department:str


@router.get("/")
def list_courses():
    return {"courses": db}

@router.post("/insert")
def add_courses(course:Course):
    db.append(course)
    return {"message": "Course added Successfully"}

