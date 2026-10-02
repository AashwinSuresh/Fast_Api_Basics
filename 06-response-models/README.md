# Lesson 06 — Response Models & Status Codes

## Overview
When building APIs, security and proper HTTP semantics are critical:
1. **Security / Data Filtering:** You often accept sensitive information from users (like passwords or tokens) or store internal fields that clients should **never** see. A **Response Model** filters out sensitive data automatically before the response leaves your server.
2. **HTTP Status Codes:** A newly created resource should return `201 Created` rather than a generic `200 OK`.

---

## Key Concepts & Code Breakdown (`main.py`)

- `from fastapi import status`  
  Provides convenient named constants for standard HTTP status codes (e.g., `status.HTTP_201_CREATED`, `status.HTTP_404_NOT_FOUND`) so you don't have to remember status numbers.

- **Separating Request and Response Models:**
  ```python
  class StudentCreate(BaseModel):
      name: str
      age: int
      password: str  # Accepted from the client

  class StudentResponse(BaseModel):
      id: int
      name: str
      age: int       # Notice: password is intentionally NOT here!
  ```

- `@app.post("/students", response_model=StudentResponse, status_code=status.HTTP_201_CREATED)`  
  - `response_model=StudentResponse`: Tells FastAPI to shape the output using `StudentResponse`. Even though `create_student` returns a dictionary containing `"password": student.password`, FastAPI automatically strips the `password` field away before sending the JSON to the client!
  - `status_code=status.HTTP_201_CREATED`: Sets the response status code to `201` (standard for creating new resources).

- `global id`  
  Increments a simple global counter to generate unique sequential IDs for each created student.

---

## How to Run

From this directory (`06-response-models`), run:

```bash
uvicorn main:app --reload
```

---

## Testing the Endpoints

Open `http://127.0.0.1:8000/docs`:

1. Send a `POST /students` request with:
   ```json
   {
     "name": "Bruce Wayne",
     "age": 30,
     "password": "batman_secret_password"
   }
   ```
2. **Check the Status Code:** Observe that the response code is `201 Created`.
3. **Check the Response Body:**
   ```json
   {
     "id": 1,
     "name": "Bruce Wayne",
     "age": 30
   }
   ```
   Notice that `password` is completely omitted from the output.
