# Lesson 05 — Pydantic Validation

Pydantic models let FastAPI validate incoming data before the route function uses it.

Field() adds extra rules to a field. min_length and max_length restrict a string, while ge and le restrict a number.

email: str | None = None makes the email optional.

If the incoming data does not satisfy the model, FastAPI returns a validation error automatically.

The backend.py file contains the temporary list used as the data store.