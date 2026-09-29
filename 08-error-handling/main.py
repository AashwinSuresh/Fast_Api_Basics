from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI(title="FastAPI Basics - Lesson 08")


# ============================================================
# 1. MODEL
# ============================================================

class Student(BaseModel):
    name: str
    age: int
    department: str


students = [
    Student(name="Rahul", age=21, department="CSE"),
    Student(name="Anu", age=20, department="ECE"),
]


# ============================================================
# 2. HTTPException
# ============================================================
# Used when WE intentionally want to return an error response.
#
# Example:
# If the student does not exist, we return 404 Not Found.


@app.get("/students/{student_id}")
def get_student(student_id: int):

    if student_id < 1 or student_id > len(students):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found"
        )

    return students[student_id - 1]


# ============================================================
# 3. ValueError
# ============================================================
# A normal Python exception.
#
# Here we intentionally raise ValueError if the age is invalid.
#
# NOTE:
# FastAPI does NOT automatically convert every Python exception
# into a nice HTTP response.
#
# An unhandled ValueError normally results in a 500 Internal
# Server Error.


@app.get("/students/check-age/{age}")
def check_age(age: int):

    if age < 0:
        raise ValueError("Age cannot be negative")

    return {
        "message": "Age is valid",
        "age": age
    }


# ============================================================
# 4. Handling an exception with try/except
# ============================================================
# Instead of allowing the Python exception to become a 500 error,
# we can catch it ourselves and return an appropriate HTTP error.


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


# ============================================================
# 5. KeyError
# ============================================================
# KeyError happens when we try to access a dictionary key
# that does not exist.


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


# ============================================================
# 6. IndexError
# ============================================================
# IndexError happens when we try to access a list position
# that does not exist.


@app.get("/students/index/{index}")
def get_student_by_index(index: int):

    try:
        return students[index]

    except IndexError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student index does not exist"
        )


# ============================================================
# 7. Request validation error
# ============================================================
# FastAPI + Pydantic automatically validate incoming data.
#
# If the client sends:
#
# {
#     "name": "Rahul",
#     "age": "hello",
#     "department": "CSE"
# }
#
# FastAPI will automatically return a validation error.
#
# We do NOT need to manually write try/except for this.


@app.post("/students")
def create_student(student: Student):

    students.append(student)

    return {
        "message": "Student created",
        "student": student
    }