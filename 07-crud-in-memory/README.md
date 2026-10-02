# Lesson 07 — CRUD API (In-Memory)

## Overview
**CRUD** stands for **C**reate, **R**ead, **U**pdate, and **D**elete — the four core operations of almost any web API.

In this lesson, you build a complete RESTful CRUD API for managing students. Instead of a database, data is stored in a Python list in memory (meaning data resets whenever the server restarts).

---

## REST Mapping Summary

| Operation | HTTP Method | Route | Status Code | Description |
| :--- | :--- | :--- | :--- | :--- |
| **Create** | `POST` | `/students` | `201 Created` | Adds a new student |
| **Read All** | `GET` | `/students` | `200 OK` | Retrieves all students |
| **Read One** | `GET` | `/students/{student_id}` | `200 OK` | Retrieves a single student by ID |
| **Update** | `PUT` | `/students/{student_id}` | `200 OK` | Updates/replaces an existing student |
| **Delete** | `DELETE` | `/students/{student_id}` | `204 No Content` | Removes a student |

---

## Key Concepts & Code Breakdown (`main.py`)

- **Model Inheritance:**
  ```python
  class StudentCreate(BaseModel):
      name: str
      age: int
      department: str

  class Student(StudentCreate):
      id: int
  ```
  `Student` inherits all fields from `StudentCreate` and adds `id`. This prevents duplicating field definitions.

- `**data.model_dump()`  
  `model_dump()` (Pydantic V2) converts the Pydantic model into a Python dictionary. The `**` operator unpacks those dictionary keys as keyword arguments to instantiate `Student(id=next_id, ...)`.

- `response_model=list[Student]`  
  Declares that the endpoint returns a list containing `Student` objects.

- `raise HTTPException(404, "Student not found")`  
  If the student ID is not found in the list, stops execution and immediately sends back an HTTP 404 response to the client.

- `status.HTTP_204_NO_CONTENT`  
  Used with `DELETE`. A `204` status code indicates success with an empty response body.

---

## How to Run

From this directory (`07-crud-in-memory`), run:

```bash
uvicorn main:app --reload
```

---

## Step-by-Step Testing via `/docs`

1. **Create:** Call `POST /students` with `{"name": "Ananya", "age": 21, "department": "ECE"}`.
2. **Read All:** Call `GET /students` and confirm Ananya is returned with `id: 1`.
3. **Read by ID:** Call `GET /students/1` to view Ananya.
4. **Update:** Call `PUT /students/1` with `{"name": "Ananya Sharma", "age": 22, "department": "ECE"}`.
5. **Delete:** Call `DELETE /students/1` (receives 204 No Content).
6. **Verify Not Found:** Call `GET /students/1` again and see the `404 Student not found` response.
