# Lesson 01 — First FastAPI App

This is the smallest FastAPI application in the course.

FastAPI() creates the application. The @app.get() decorators connect URLs to Python functions. Returning a dictionary makes FastAPI send a JSON response.

The application also provides automatic API documentation at /docs.

Run: uvicorn main:app --reload