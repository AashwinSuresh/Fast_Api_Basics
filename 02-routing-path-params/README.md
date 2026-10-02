# Lesson 02 — Routing & Path Parameters

## Overview
Web applications often need dynamic URLs — such as fetching a user profile by ID (`/users/1`) or a product page by slug (`/products/laptop`).

This lesson covers **Path Parameters**: how to capture dynamic values from the URL path, pass them into your Python function, and automatically validate their data types.

---

## Key Concepts & Code Breakdown (`main.py`)

- `@app.get("/students")`  
  A standard static GET route returning a hardcoded list of student names.

- `@app.get("/students/{student_id}")`  
  The curly braces `{student_id}` define a **path parameter**. Whatever value the user types in that position of the URL will be captured.

- `def get_student(student_id: int):`  
  Notice the parameter name matches `{student_id}` in the route decorator, and it includes a Python type hint: `: int`.
  
  FastAPI does two magical things with this type hint:
  1. **Automatic Type Conversion:** Even though URLs are always sent as strings (e.g., `"/students/42"`), FastAPI converts `"42"` into the Python integer `42`.
  2. **Automatic Data Validation:** If a user navigates to `/students/hello`, FastAPI immediately stops the request and returns a `422 Unprocessable Entity` error stating that `student_id` must be an integer.

- `return {"student_id": student_id, "name": f"Student {student_id}"}`  
  Returns a dynamic JSON response combining the parsed ID and formatted string.

---

## How to Run

From this directory (`02-routing-path-params`), run:

```bash
uvicorn main:app --reload
```

---

## Testing the Endpoints

1. **Get student list:**
   - URL: `http://127.0.0.1:8000/students`
   - Response: `{"students": ["Asha", "Rahul", "Maya"]}`

2. **Valid path parameter:**
   - URL: `http://127.0.0.1:8000/students/3`
   - Response: `{"student_id": 3, "name": "Student 3"}`

3. **Invalid path parameter (Try this!):**
   - URL: `http://127.0.0.1:8000/students/abc`
   - Response: HTTP 422 with a message stating that `value is not a valid integer`.
