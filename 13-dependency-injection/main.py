from fastapi import Depends, FastAPI

app = FastAPI(title="FastAPI Basics - Lesson 13")

def common_parameters(page: int , limit: int):
    return {"page": page, "limit": limit,"message": "This is from dependency injection"}


@app.get("/students")
def list_students(params: dict = Depends(common_parameters)):
    return {"output": params}
