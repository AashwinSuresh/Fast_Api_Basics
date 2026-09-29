from fastapi import FastAPI

app = FastAPI(title="FastAPI Basics - Lesson 03")

@app.get("/students")
def list_students(department: str | None = None, year: int | None = None):
    students = [
        {"id": 1, "name": "Asha", "department": "CSE", "year": 2},
        {"id": 2, "name": "Rahul", "department": "ECE", "year": 3},
        {"id": 3, "name": "Maya", "department": "CSE", "year": 4},
    ]
    if department is not None and year is not None:
        students = [s for s in students if s['department']==department and s['year']==year]
    else:
        if department is not None:
            students = [s for s in students if s["department"] == department]
        if year is not None:
            students = [s for s in students if s["year"] == year]
    return {"count": len(students), "students": students}
