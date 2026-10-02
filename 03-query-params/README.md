# Lesson 03 — Query Parameters

Query parameters are values added after ? in a URL.

In this example, department and year are optional filters. The str | None = None and int | None = None annotations mean that either value may be missing.

The code applies whichever filters were provided.

Try /students?department=CSE&year=4.