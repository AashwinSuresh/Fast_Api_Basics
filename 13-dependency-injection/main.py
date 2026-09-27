from fastapi import Depends, FastAPI

app = FastAPI(title="FastAPI Basics - Lesson 13")

def common_parameters(page: int = 1, limit: int = 10):
    return {"page": page, "limit": limit}

@app.get("/students")
def list_students(params: dict = Depends(common_parameters)):
    return {"filters": params}
