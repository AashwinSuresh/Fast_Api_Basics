from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="FastAPI Basics - Lesson 04")

class Student(BaseModel):
    name: str
    age: int
    department: str

@app.post("/students")
def create_student(student: Student):
    return {"message": "Student received", "student": student}
