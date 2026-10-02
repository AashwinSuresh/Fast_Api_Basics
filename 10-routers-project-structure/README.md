# Lesson 13 — Project Structure and APIRouter

As an API grows, keeping every route in one file becomes difficult to manage. APIRouter lets us group related routes into separate modules.

students.py and courses.py each contain their own router. prefix adds a common part to their URLs, while tags groups them in Swagger documentation.

app/main.py creates the FastAPI application and uses include_router() to add those routes.

The __init__.py files make the folders Python packages. The router package's __init__.py also contains the temporary data lists used by the examples.

Run from this folder:

uvicorn app.main:app --reload