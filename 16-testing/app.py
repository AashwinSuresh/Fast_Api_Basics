from fastapi import FastAPI

app = FastAPI(title="FastAPI Basics - Lesson 16")

@app.get("/")
def home():
    return {"message": "hello"}
