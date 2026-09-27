from fastapi import FastAPI
from app.routers import students, courses

app = FastAPI(title="FastAPI Basics - Lesson 10")
app.include_router(students.router)
app.include_router(courses.router)
