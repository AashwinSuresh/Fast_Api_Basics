# Lesson 03 — Query Parameters

## Overview
While path parameters identify a specific resource (`/students/1`), **query parameters** are used to filter, sort, paginate, or customize lists of resources.

In URLs, query parameters appear after a question mark `?` and are separated by `&`, for example:  
`/students?department=CSE&year=4`

---

## Key Concepts & Code Breakdown (`main.py`)

- **How FastAPI recognizes query parameters:**  
  When function arguments are **not** defined inside the path decorator (like `{student_id}` was in Lesson 02), FastAPI automatically treats them as **query parameters**.

- `def list_students(department: str | None = None, year: int | None = None):`  
  - `department: str | None = None` defines an optional string parameter. If the client doesn't pass `?department=...`, it defaults to `None`.
  - `year: int | None = None` defines an optional integer parameter. FastAPI converts the query string value (e.g. `?year=2`) into an integer and validates that it is a valid number.
  - The `| None = None` syntax (Python 3.10+) makes these parameters completely optional. Without default values, FastAPI would require them in the URL.

- **Filtering Logic:**  
  The Python code uses list comprehensions to check if `department` or `year` were supplied, narrowing down the returned results.

- `return {"count": len(students), "students": students}`  
  Returns both the total count of matched results and the filtered student list.

---

## How to Run

From this directory (`03-query-params`), run:

```bash
uvicorn main:app --reload
```

---

## Testing the Endpoints

Try navigating to these URLs in your browser or through `/docs`:

1. **All students (no filters):**  
   `http://127.0.0.1:8000/students`
2. **Filter by department only:**  
   `http://127.0.0.1:8000/students?department=CSE`
3. **Filter by year only:**  
   `http://127.0.0.1:8000/students?year=3`
4. **Combine multiple query parameters:**  
   `http://127.0.0.1:8000/students?department=CSE&year=4`
