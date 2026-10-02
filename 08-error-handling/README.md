# Lesson 08 — Error Handling

## Overview
Errors happen in every application: users request things that don't exist, provide invalid input, or perform impossible operations (like dividing by zero).

In Python scripts, unhandled exceptions simply crash the script. In a web API, an unhandled exception results in an ugly **500 Internal Server Error**. This lesson demonstrates how to handle errors cleanly using FastAPI's `HTTPException` and `try/except` blocks.

---

## Key Concepts & Code Breakdown (`main.py`)

- `from fastapi import HTTPException, status`  
  `HTTPException` is the standard exception class used by FastAPI to return HTTP error responses with status codes and JSON error details.

- **Raising Intentional HTTP Errors:**
  ```python
  if student_id < 1 or student_id > len(students):
      raise HTTPException(
          status_code=status.HTTP_404_NOT_FOUND,
          detail="Student not found"
      )
  ```
  Immediately halts execution and returns:
  ```json
  {
    "detail": "Student not found"
  }
  ```

- **Catching Python Exceptions with `try / except`:**
  - **`ZeroDivisionError` → `400 Bad Request`:**
    ```python
    try:
        result = 100 / number
    except ZeroDivisionError:
        raise HTTPException(status_code=400, detail="Cannot divide by zero")
    ```
  - **`KeyError` → `404 Not Found`:**  
    Caught when accessing a dictionary key that does not exist (`student[field]`).
  - **`IndexError` → `404 Not Found`:**  
    Caught when trying to access a list item at an index out of bounds.

- **Automatic Validation Errors (HTTP 422):**  
  For request body validation (like passing `"hello"` for `age: int`), FastAPI handles the error automatically without needing any `try/except` code.

---

## How to Run

From this directory (`08-error-handling`), run:

```bash
uvicorn main:app --reload
```

---

## Testing Error Scenarios in `/docs`

| Route | Test Input | Expected Result | Why |
| :--- | :--- | :--- | :--- |
| `GET /students/{id}` | `id = 999` | `404 Not Found` | Explicit `HTTPException` raised |
| `GET /students/divide/{num}` | `num = 0` | `400 Bad Request` | Caught `ZeroDivisionError` |
| `GET /student-info/{field}` | `field = salary` | `404 Not Found` | Caught `KeyError` |
| `GET /students/index/{idx}` | `idx = 50` | `404 Not Found` | Caught `IndexError` |
| `POST /students` | `age = "abc"` | `422 Unprocessable` | Automatic Pydantic validation |
