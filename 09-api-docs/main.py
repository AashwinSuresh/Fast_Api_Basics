from fastapi import FastAPI

app = FastAPI(title="FastAPI Basics - Lesson 09", version="1.0.0")

@app.get("/hello", tags=["Demo"])
def hello():
    return {"message": "Explore this endpoint through Swagger UI"}
