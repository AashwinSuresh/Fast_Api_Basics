# Lesson 12 — Mini Project

This is a small end-to-end example where a simple HTML page communicates with a FastAPI backend.

The backend provides endpoints for viewing and creating students. The frontend uses JavaScript fetch() to send HTTP requests and read JSON responses.

The backend uses Pydantic models and a Python list as temporary storage.

CORSMiddleware allows the browser page to communicate with the API even though the frontend and backend run on different origins.

Run the backend with FastAPI, then serve index.html separately, for example with:

python -m http.server 3000

The important idea is the communication between the frontend and the FastAPI API.