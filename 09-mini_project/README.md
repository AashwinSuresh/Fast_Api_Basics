# Lesson 09 — Full-Stack Mini Project

## Overview
Up until now, we tested our APIs through Swagger UI (`/docs`). In the real world, APIs serve web or mobile applications.

This mini project brings everything together by connecting a **Vanilla HTML/JavaScript frontend** (`index.html`) to our **FastAPI backend** (`main.py`).

---

## Key Concepts & Code Breakdown

### 1. Backend (`main.py`)
- `CORSMiddleware` & `app.add_middleware()`:  
  Browsers enforce security policies that block web pages on one origin (or local file) from talking to an API on another port. Adding `CORSMiddleware` with `allow_origins=["*"]` allows the frontend to call our FastAPI server.
- `GET /students`:  
  Returns the current list of students.
- `POST /students`:  
  Accepts a `StudentCreate` JSON payload, creates a `Student` with an auto-incremented ID, stores it in `students`, and returns the created student object.

### 2. Frontend (`index.html`)
- `fetch("http://localhost:8000/students")`:  
  Uses the browser's native JavaScript `fetch` API to make an asynchronous `GET` request to FastAPI.
- `fetch("http://localhost:8000/students", { method: "POST", ... })`:  
  Sends a `POST` request with headers `Content-Type: application/json` and the request body converted to a JSON string with `JSON.stringify()`.
- Dynamic DOM Updates:  
  `document.createElement("li")` and `list.appendChild(item)` update the UI instantly without needing a full page reload.

---

## How to Run

### Step 1: Start the FastAPI Backend
From this directory (`09-mini_project`), start the backend server:

```bash
uvicorn main:app --reload
```
The backend is now live at `http://127.0.0.1:8000`.

### Step 2: Open the Frontend
Open `index.html` in your browser:
- You can simply double-click `index.html` in your file explorer, or
- Right-click `index.html` in VS Code and choose **Open with Live Server** (or open in default browser).

---

## How to Test
1. Look at the webpage: the student list initially loads empty (or shows current students).
2. Enter a student name (e.g. `Rohan`) and age (e.g. `20`).
3. Click **Add Student**.
4. The student is sent to FastAPI, stored in memory, and instantly appears on the webpage!
