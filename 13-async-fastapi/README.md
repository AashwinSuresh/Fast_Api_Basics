# Lesson 13 — Async FastAPI

## Overview
Earlier in Lesson 00, we learned the fundamentals of asynchronous Python. In this lesson, we connect those concepts directly to FastAPI by writing **`async def`** endpoints.

Web applications spend most of their time waiting: waiting for a database to answer, waiting for a microservice to respond, or waiting for a third-party API. With `async def`, FastAPI can handle thousands of concurrent requests without locking up worker threads while waiting.

---

## Key Concepts & Code Breakdown (`main.py`)

- **Simulating I/O-Bound Operations:**
  ```python
  async def get_student_data():
      await asyncio.sleep(2)
      return "Student data"

  async def get_course_data():
      await asyncio.sleep(2)
      return "Course data"
  ```
  `asyncio.sleep(2)` simulates an external non-blocking network or database call that takes 2 seconds.

- `@app.get("/async-demo") async def async_demo():`  
  By declaring the endpoint as `async def`, FastAPI runs it directly inside the asynchronous event loop.

- `student_data, course_data = await asyncio.gather(...)`  
  Triggers both `get_student_data()` and `get_course_data()` simultaneously:
  - If executed sequentially (synchronously), it would take 2 + 2 = 4 seconds.
  - With `asyncio.gather()`, both 2-second waits happen concurrently, finishing in just **~2 seconds** total!

- `time.perf_counter()`  
  High-resolution timer used to benchmark exact execution duration and return `"time_taken"`.

---

## When Should You Use `async def` vs Normal `def`?

- **Use `async def`** when your code calls async libraries with `await` (such as `httpx.AsyncClient`, async database drivers like `asyncpg`, or redis).
- **Use standard `def`** when using synchronous libraries (like `requests` or standard `sqlite3`). FastAPI automatically runs normal `def` functions in a separate background threadpool so they don't block the event loop!

---

## How to Run

From this directory (`13-async-fastapi`), run:

```bash
uvicorn main:app --reload
```

---

## Testing the Endpoint

1. Navigate to `http://127.0.0.1:8000/async-demo`.
2. Look at the terminal console: both tasks start and finish together.
3. Observe the JSON response:
   ```json
   {
     "student_data": "Student data",
     "course_data": "Course data",
     "time_taken": 2.01
   }
   ```
   Both 2-second tasks finished concurrently in ~2 seconds!
