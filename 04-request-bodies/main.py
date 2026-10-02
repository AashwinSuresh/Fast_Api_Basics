from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="FastAPI Basics - Lesson 04")

class Student(BaseModel):
    name: str
    age: int 
    department: str

database = []
@app.post("/students")
def create_student(student: Student):
    database.append(student)
    return {"message": "Student received", "student": student}

@app.get('/show/students')
def show_students():
    return database
