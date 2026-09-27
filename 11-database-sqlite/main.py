from fastapi import FastAPI

app = FastAPI(title="FastAPI Basics - Lesson 11")

@app.get("/")
def home():
    return {"message": "Next step: replace temporary data with SQLite"}
