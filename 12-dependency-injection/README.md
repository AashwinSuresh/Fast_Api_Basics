# Lesson 12 — Dependency Injection

## Overview
**Dependency Injection (DI)** sounds intimidating, but the concept is very simple:  
Instead of a function creating or fetching things it needs (like database connections, security checks, or query parameters) inside its own body, it declares them as parameters and lets the framework **"inject"** them automatically.

FastAPI has one of the cleanest and most powerful dependency injection systems of any web framework, powered by `Depends()`.

---

## Key Concepts & Code Breakdown (`main.py`)

- `from fastapi import Depends`  
  Imports the `Depends` function, which marks a parameter as a dependency that FastAPI must resolve.

- **Defining a Dependency:**
  ```python
  def common_parameters(page: int, limit: int):
      return {
          "page": page,
          "limit": limit,
          "message": "This is from dependency injection"
      }
  ```
  This is a regular Python function that expects `page` and `limit`. Since it is not decorated with `@app.get`, FastAPI doesn't expose it as a route directly.

- **Injecting the Dependency into an Endpoint:**
  ```python
  @app.get("/students")
  def list_students(params: dict = Depends(common_parameters)):
      return {"output": params}
  ```
  When a user requests `GET /students?page=1&limit=10`:
  1. FastAPI recognizes `Depends(common_parameters)`.
  2. FastAPI inspects `common_parameters`, notices it needs `page` and `limit`, and extracts them from the request query string.
  3. FastAPI runs `common_parameters(page=1, limit=10)`.
  4. The returned dictionary is passed into `list_students` as the `params` argument.

- **Why is this so useful?**
  - **Reusability:** You can add `params = Depends(common_parameters)` to 50 different endpoints (courses, books, orders) without rewriting pagination logic.
  - **Modularity:** In real apps, `Depends()` is used to open database sessions, verify JWT authentication tokens, check user roles, and enforce rate limits.

---

## How to Run

From this directory (`12-dependency-injection`), run:

```bash
uvicorn main:app --reload
```

---

## Testing the Endpoint

1. **Request with pagination query params:**  
   `http://127.0.0.1:8000/students?page=2&limit=25`

2. **Expected Response:**
   ```json
   {
     "output": {
       "page": 2,
       "limit": 25,
       "message": "This is from dependency injection"
     }
   }
   ```
3. Open `http://127.0.0.1:8000/docs` to see how Swagger automatically detects the query parameters needed by `common_parameters` and provides input fields for them!
