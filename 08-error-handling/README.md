# Lesson 08 — Error Handling

An API should give a useful response when something goes wrong.

HTTPException is used when the application intentionally needs to return an HTTP error. The example uses it for a missing student, missing dictionary field, invalid list index, and division by zero.

ValueError, KeyError, and IndexError are normal Python exceptions. try/except lets the application catch them and turn them into a useful HTTP response.

Pydantic validation is handled by FastAPI automatically, so invalid request data does not need its own try/except.