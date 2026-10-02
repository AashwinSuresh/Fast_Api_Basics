# Lesson 16 — Async FastAPI

An async def FastAPI route can use asynchronous operations without blocking while it waits.

The two helper functions simulate I/O work with asyncio.sleep(2). In a real application, the waiting could come from a database, another API, or a network operation.

asyncio.gather() runs both operations concurrently, so the example can complete in roughly the time of the longer operation rather than waiting for each one separately.

time.perf_counter() measures the elapsed time accurately.