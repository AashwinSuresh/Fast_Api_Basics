from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI(title="FastAPI Basics - Lesson 07")

class StudentCreate(BaseModel):
    name: str
    age: int
    department: str

class Student(StudentCreate):
    id: int

students: list[Student] = []
next_id = 1

@app.post("/students", response_model=Student, status_code=status.HTTP_201_CREATED)
def create_student(data: StudentCreate):
    global next_id
    student = Student(id=next_id, **data.model_dump())
    students.append(student)
    next_id += 1
    return student

@app.get("/students", response_model=list[Student])
def list_students():
    return students

@app.get("/students/{student_id}", response_model=Student)
def get_student(student_id: int):
    for student in students:
        if student.id == student_id:
            return student
    raise HTTPException(404, "Student not found")

@app.put("/students/{student_id}", response_model=Student) #replace
def update_student(student_id: int, data: StudentCreate):
    for i,student in enumerate(students):
        if student.id == student_id:
            updated = Student(id=student_id, **data.model_dump())
            students[i] = updated
            return updated
    raise HTTPException(404, "Student not found")

@app.delete("/students/{student_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_student(student_id: int):
    for i,student in enumerate(students):
        if student.id == student_id:
            students.pop(i)
            return
    raise HTTPException(404, "Student not found")
