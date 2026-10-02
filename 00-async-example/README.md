# Lesson 00 — Async Python Foundation

## Overview
FastAPI is built on top of **asynchronous Python** (`asyncio`). Before diving into web endpoints, this lesson demonstrates how Python handles multiple tasks concurrently without blocking the entire program.

In traditional (synchronous) code, if a function waits for something (like a database query or network response), the whole program freezes until it finishes. With async Python, while one task is waiting, Python switches to work on another task.

---

## Key Concepts & Code Breakdown (`test01.py`)

Here are the new concepts and lines used in this lesson:

- `async def task1():`  
  Declares a **coroutine**. Unlike a normal function, calling an async function does not run it immediately; it returns a coroutine object that can be paused and resumed.

- `await asyncio.sleep(3)`  
  The `await` keyword tells Python: *"Pause this task here while waiting, and let other tasks run in the meantime."*  
  `asyncio.sleep(3)` simulates a 3-second non-blocking delay (such as waiting for a database or API response).

- `await asyncio.gather(task1(), task2(), task3())`  
  Runs multiple async tasks **concurrently** (at the same time). It waits until all three tasks have finished before moving to the next line.

- `asyncio.run(main())`  
  The entry point of an asyncio program. It creates the event loop, runs the `main()` coroutine to completion, and cleans up.

---

## How to Run

Navigate into this folder and run:

```bash
python test01.py
```

### Expected Output
Notice how `task1` and `task2` start, print their first iteration, and then both sleep together. Rather than taking 6 + 6 = 12 seconds sequentially, all tasks complete in approximately **6 seconds** because they wait concurrently.
