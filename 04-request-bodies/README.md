# Lesson 04 — Request Bodies

## Overview
When you need to send structured data to a server (like registering a user or creating an order), sending data in the URL is not enough. You send it inside the **HTTP Request Body** as JSON.

FastAPI uses **Pydantic models** to parse the incoming JSON, validate that all required fields are present and of the right type, and give you clean Python objects.

---

## Key Concepts & Code Breakdown (`main.py`)

- `from pydantic import BaseModel`  
  Imports Pydantic's base schema class. Pydantic is the engine behind FastAPI's data validation and parsing.

- `class Student(BaseModel):`  
  Defines the schema for the request body:
  ```python
  name: str
  age: int 
  department: str
  ```
  FastAPI will expect incoming JSON to match this shape:
  ```json
  {
    "name": "Alice",
    "age": 20,
    "department": "CSE"
  }
  ```

- `@app.post("/students")`  
  Uses the HTTP `POST` method, which is the REST convention for submitting data to create a new resource.

- `def create_student(student: Student):`  
  Because `Student` is a subclass of `BaseModel`, FastAPI knows to read the JSON payload from the request body, validate every field, and pass the validated object to your function as `student`.

- `database.append(student)`  
  Appends the validated student object to an in-memory Python list serving as a temporary store.

- `@app.get('/show/students')`  
  A simple GET endpoint that returns all student records currently stored in the in-memory list.

### Additional Payload Types in `main.py` (Commented Reference):
- `Body()`: Used to accept individual JSON fields or raw dictionaries directly without defining a full Pydantic class.
- `Form()`: Used when data is submitted from a traditional HTML `<form>` (`application/x-www-form-urlencoded`).
- `UploadFile` / `File()`: Used for handling file uploads in memory or spooled disk files.

---

## How to Run

From this directory (`04-request-bodies`), run:

```bash
uvicorn main:app --reload
```

---

## Testing via Swagger UI (`/docs`)

1. Open `http://127.0.0.1:8000/docs` in your browser.
2. Find the `POST /students` endpoint, click **Try it out**.
3. FastAPI pre-populates an example JSON body based on your Pydantic model:
   ```json
   {
     "name": "Alice",
     "age": 21,
     "department": "CSE"
   }
   ```
4. Click **Execute** and observe the 200 response.
5. Then execute `GET /show/students` to see your newly created student in the list!
