from fastapi import FastAPI

app = FastAPI(title="FastAPI Basics - Lesson 02")

@app.get("/students")
def get_students():
    return {"students": ["Asha", "Rahul", "Maya"]}

@app.get("/students/{student_id}")
def get_student(student_id : int):
    return {"student_id": student_id, "name": f"Student {student_id}"}
