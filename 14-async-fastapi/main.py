import asyncio
from fastapi import FastAPI

app = FastAPI(title="FastAPI Basics - Lesson 14")

async def pretend_io_work():
    await asyncio.sleep(1)
    return "I/O work finished"

@app.get("/async-demo")
async def async_demo():
    result = await pretend_io_work()
    return {"result": result}
