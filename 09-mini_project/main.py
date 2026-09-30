from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


app = FastAPI()


# Allow our frontend to communicate with the backend.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


# -----------------------------
# Student models
# -----------------------------

class StudentCreate(BaseModel):
    name: str
    age: int


class Student(BaseModel):
    id: int
    name: str
    age: int


# -----------------------------
# Temporary database
# -----------------------------
# We are just using a Python list.
# The data will disappear when the server restarts.

students: list[Student] = []


# -----------------------------
# Get all students
# -----------------------------

@app.get("/students")
def get_students():
    return students


# -----------------------------
# Create a student
# -----------------------------

@app.post("/students")
def create_student(data: StudentCreate):

    new_student = Student(
        id=len(students) + 1,
        name=data.name,
        age=data.age
    )

    students.append(new_student)

    # We return the ACTUAL student data,
    # not just "Student created".
    return new_student