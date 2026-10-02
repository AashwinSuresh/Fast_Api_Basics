# Lesson 15 — Dependency Injection

Dependency injection lets a route receive something that another function has prepared.

Depends(common_parameters) tells FastAPI to call common_parameters before running the route and pass its result into params.

This is useful when the same logic is needed by several routes. Instead of repeating that logic, it can be placed in one dependency and reused.

The same pattern is commonly used for database sessions, authentication checks, and shared request parameters.