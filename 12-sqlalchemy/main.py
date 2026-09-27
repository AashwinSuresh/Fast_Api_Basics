from fastapi import FastAPI

app = FastAPI(title="FastAPI Basics - Lesson 12")

@app.get("/")
def home():
    return {"message": "SQLAlchemy lesson starter"}
