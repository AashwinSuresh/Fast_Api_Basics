from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI(title="FastAPI Basics - Lesson 08")

class Student(BaseModel):
    name: str
    age: int
    department: str


students = [
    Student(name="Rahul", age=21, department="CSE"),
    Student(name="Anu", age=20, department="ECE"),
]


@app.get("/students/{student_id}")
def get_student(student_id: int):

    if student_id < 1 or student_id > len(students):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found"
        )

    return students[student_id - 1]


@app.get("/students/check-age/{age}")
def check_age(age: int):

    if age < 0:
        raise ValueError("Age cannot be negative")

    return {
        "message": "Age is valid",
        "age": age
    }


@app.get("/students/divide/{number}")
def divide(number: int):

    try:
        result = 100 / number

        return {
            "result": result
        }

    except ZeroDivisionError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Cannot divide by zero"
        )


@app.get("/student-info/{field}")
def get_student_info(field: str):

    student = {
        "name": "Rahul",
        "age": 21,
        "department": "CSE"
    }

    try:
        return {
            "value": student[field]
        }

    except KeyError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Field '{field}' not found"
        )


@app.get("/students/index/{index}")
def get_student_by_index(index: int):

    try:
        return students[index]

    except IndexError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student index does not exist"
        )


@app.post("/students")
def create_student(student: Student):

    students.append(student)

    return {
        "message": "Student created",
        "student": student
    }
