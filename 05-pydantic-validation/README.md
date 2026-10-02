# Lesson 05 — Pydantic Validation

## Overview
Checking data types (like verifying age is an integer) is only half the battle. In real applications, you also need **business rules and constraints**:
- A name shouldn't be empty or 500 characters long.
- A student's age shouldn't be negative or 150.
- Certain fields should be optional while others are strictly required.

This lesson shows how to enforce these rules automatically using Pydantic's `Field()`.

---

## Key Concepts & Code Breakdown (`main.py`)

- `from pydantic import BaseModel, Field`  
  Imports `Field`, which provides fine-grained validation constraints and metadata for model attributes.

- `from backend import database as db`  
  Imports the shared list from `backend.py`, keeping the data storage separated from the route handlers.

- `class StudentCreate(BaseModel):`  
  - `name: str = Field(min_length=2, max_length=50)`  
    Ensures the name is between 2 and 50 characters long. Values like `""` or `"A"` are rejected immediately.
  - `age: int = Field(ge=16, le=100)`  
    Enforces numeric boundaries:
    - `ge=16`: **G**reater than or **E**qual to 16.
    - `le=100`: **L**ess than or **E**qual to 100.
    Ages like `-5` or `120` are rejected automatically.
  - `department: str`  
    A required string field without extra constraints.
  - `email: str | None = None`  
    An optional field that defaults to `None` if not provided in the request body.

- **Automatic HTTP 422 Validation Error:**  
  You do not need to write manual `if age < 16:` checks. If the client sends invalid data, FastAPI returns a detailed HTTP 422 response specifying the exact field and error message.

---

## How to Run

From this directory (`05-pydantic-validation`), run:

```bash
uvicorn main:app --reload
```

---

## Testing the Endpoints

Open `http://127.0.0.1:8000/docs`:

1. **Test Valid Input:**
   ```json
   {
     "name": "Jane Doe",
     "age": 22,
     "department": "Mechanical",
     "email": "jane@example.com"
   }
   ```
   Result: `200 OK` with `"message": "Validated successfully"`.

2. **Test Invalid Input (Watch Pydantic catch it!):**
   ```json
   {
     "name": "J",
     "age": 12,
     "department": "Mechanical"
   }
   ```
   Result: `422 Unprocessable Entity` highlighting both that `name` is too short (< 2) and `age` is too small (< 16).
