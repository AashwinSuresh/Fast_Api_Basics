# Lesson 10 — Project Structure & APIRouter

## Overview
As web applications grow, keeping all models and routes in a single `main.py` file quickly becomes disorganized and difficult to maintain.

FastAPI provides **`APIRouter`** to divide your API into modular, reusable mini-routers — similar to blueprints in Flask or controllers in other frameworks.

---

## Project Directory Structure

```text
10-routers-project-structure/
├── app/
│   ├── __init__.py
│   ├── main.py              # Main entry point; includes all routers
│   └── routers/
│       ├── __init__.py      # In-memory storage lists
│       ├── students.py      # Student-related routes (/students)
│       └── courses.py       # Course-related routes (/courses)
└── README.md
```

---

## Key Concepts & Code Breakdown

### 1. Defining a Router (`students.py` & `courses.py`)
- `from fastapi import APIRouter`  
  Imports the router class used to group related path operations.

- `router = APIRouter(prefix="/students", tags=["Students"])`  
  - `prefix="/students"`: Automatically prepends `/students` to every route in this file. A route defined as `@router.get("/")` will automatically be served at `/students/`.
  - `tags=["Students"]`: Groups all these routes under a clean, labeled "Students" section in Swagger UI (`/docs`).

- `@router.get("/")` and `@router.post("/insert")`  
  Notice we use `@router` instead of `@app` because the router operates independently of the main app until it is mounted.

### 2. Including Routers in the App (`app/main.py`)
- `app.include_router(students.router)` & `app.include_router(courses.router)`  
  Mounts each router onto the primary `FastAPI` instance. The main application stays clean, acts as an orchestrator, and delegates specific duties to routers.

---

## How to Run

From this directory (`10-routers-project-structure`), run:

```bash
uvicorn app.main:app --reload
```

> **Note:** We specify `app.main:app` because `main.py` is located inside the `app` folder.

---

## Testing in Swagger Docs

Visit `http://127.0.0.1:8000/docs`:
- Notice the UI is neatly categorized into **Students** and **Courses** sections.
- Test `POST /students/insert` and `GET /students/`.
- Test `POST /courses/insert` and `GET /courses/`.
