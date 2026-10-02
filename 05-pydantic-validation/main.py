from fastapi import FastAPI
from pydantic import BaseModel, Field
from backend import database as db
app = FastAPI(title="FastAPI Basics - Lesson 05")

class StudentCreate(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    age: int = Field(ge=16, le=100)
    department: str
    email: str | None = None

@app.post("/students")
def create_student(student: StudentCreate):
    db.append(student)
    return {"message": "Validated successfully", "student": student}

@app.get('/show_students')
def show_studs():
    return db



