# Lesson 01 — First FastAPI App

## Overview
This lesson demonstrates the absolute foundation of FastAPI: creating an application instance, registering HTTP `GET` endpoints, returning JSON responses, and running the server with Uvicorn.

FastAPI is designed to be fast, easy to learn, and comes with automatic interactive documentation out of the box.

---

## Key Concepts & Code Breakdown (`main.py`)

- `from fastapi import FastAPI`  
  Imports the core `FastAPI` class used to initialize your web server application.

- `app = FastAPI(title="FastAPI Basics - Lesson 01")`  
  Creates the application instance named `app`. The `title` parameter customizes the name displayed in the automatic Swagger documentation.

- `@app.get("/")`  
  A **route decorator** (path operation decorator). It tells FastAPI: *"When an HTTP `GET` request is made to the root path `/`, run the function below."*

- `def home():`  
  The path operation function. Whenever `/` is requested, this function executes.

- `return {"message": "Hello, FastAPI!"}`  
  FastAPI automatically converts Python dictionaries into standard **JSON** format and sets the `Content-Type: application/json` header for you.

- `@app.get("/about")`  
  Creates a second route at the `/about` URL path, returning metadata about the current lesson.

---

## How to Run

From this directory (`01-first-fastapi-app`), run:

```bash
uvicorn main:app --reload
```

- `main`: points to the Python file `main.py`.
- `app`: points to the `app = FastAPI()` object inside `main.py`.
- `--reload`: enables auto-reload so the server refreshes whenever you save changes.

---

## Testing the Endpoints

Open your browser or API client to:
- `http://127.0.0.1:8000/` → Returns `{"message": "Hello, FastAPI!"}`
- `http://127.0.0.1:8000/about` → Returns `{"lesson": 1, "topic": "First FastAPI App"}`
- `http://127.0.0.1:8000/docs` → Opens the interactive **Swagger UI** where you can test each endpoint directly!
