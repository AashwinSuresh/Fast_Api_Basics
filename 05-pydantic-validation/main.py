from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="FastAPI Basics - Lesson 05")

class StudentCreate(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    age: int = Field(ge=16, le=100)
    department: str
    email: str | None = None

@app.post("/students")
def create_student(student: StudentCreate):
    return {"message": "Validated successfully", "student": student}
