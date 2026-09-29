from fastapi import APIRouter
from pydantic import BaseModel
from routers import student_db as db
router = APIRouter(prefix="/students", tags=["Students"])

class Student(BaseModel):
    name:str
    age:int
    department:str


@router.get("/")
def list_students():
    return {"students": db}

@router.post("/insert")
def add_students(student:Student):
    db.append(student)
    return {"message": "Added student"}


