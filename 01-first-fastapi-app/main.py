from fastapi import FastAPI

app = FastAPI(title="FastAPI Basics - Lesson 01")

@app.get("/")
def home():
    return {"message": "Hello, FastAPI!"}

@app.get("/about")
def about():
    return {"lesson": 1, "topic": "First FastAPI App"}
