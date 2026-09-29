from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI(title="FastAPI Basics - Lesson 06")

class StudentCreate(BaseModel):
    name: str
    age: int
    password: str

class StudentResponse(BaseModel):
    id: int
    name: str
    age: int

id = 0

@app.post("/students", response_model=StudentResponse, status_code=status.HTTP_201_CREATED)
def create_student(student: StudentCreate):
    global id
    id+=1
    return {"id": id, "name": student.name, "age": student.age, "password": student.password}
