from fastapi import FastAPI
from pydantic import BaseModel, Field

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


#OTHER EXAMPLES :
 
#EXAMPLE - 1 💫
# from fastapi import Body

# Expects JSON: {"name": "Alice", "age": 20}
# @app.post("/students")
# def create_student(name: str = Body(), age: int = Body()):
#     return {"name": name, "age": age}

# # Or accept any freeform dictionary:
# @app.post("/raw-student")
# def create_raw(data: dict = Body()):
#     return data

#EXAMPLE - 2 💫
# from fastapi import Form

# @app.post("/login")
# def login(username: str = Form(), password: str = Form()):
#     return {"user added": username}

#EXAMPLE  3 💫
# from fastapi import FastAPI, UploadFile, File

# app = FastAPI()

# @app.post("/upload")
# async def upload_document(file: UploadFile = File(...)):
#     # Read the file's contents into memory
#     contents = await file.read()
    
#     return {
#         "filename": file.filename,
#         "content_type": file.content_type,
#         "size_bytes": len(contents),
#     }