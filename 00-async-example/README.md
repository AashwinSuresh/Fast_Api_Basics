# Async/Await Foundation

This folder introduces Python's asyncio before using async code with FastAPI.

The three tasks are asynchronous functions. await asyncio.sleep() pauses the current task without blocking the other tasks. asyncio.gather() starts the three tasks together and waits until all of them finish.

asyncio.run(main()) starts the event loop and runs the main coroutine.

Run: python test01.py

The example shows how several waiting operations can be handled concurrently.