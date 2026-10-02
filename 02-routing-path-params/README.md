# Lesson 02 — Routing and Path Parameters

A route connects an HTTP method and URL to a Python function.

The {student_id} part of /students/{student_id} is a path parameter. FastAPI takes the value from the URL and passes it to the function.

Because student_id is annotated as int, FastAPI also converts and validates the value.

Try /students and /students/2.