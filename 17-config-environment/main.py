import os
from fastapi import FastAPI

app = FastAPI(title=os.getenv("APP_NAME", "FastAPI Basics"))

@app.get("/")
def home():
    return {"app_name": app.title}
