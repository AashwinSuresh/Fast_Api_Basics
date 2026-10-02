import asyncio
import time

from fastapi import FastAPI

app = FastAPI(title="FastAPI Basics - Lesson 14")


# ------------------------------------------------------------
# FAKE I/O OPERATIONS
# ------------------------------------------------------------
# These simulate operations that take time, such as:
# - waiting for a database
# - waiting for another API
# - waiting for a network request
#
# asyncio.sleep() is used only to simulate that waiting.


async def get_student_data():
    print("Student data: started")

    await asyncio.sleep(2)

    print("Student data: finished")

    return "Student data"


async def get_course_data():
    print("Course data: started")

    await asyncio.sleep(2)

    print("Course data: finished")

    return "Course data"


# ------------------------------------------------------------
# FASTAPI ENDPOINT
# ------------------------------------------------------------

@app.get("/async-demo")
async def async_demo():

    start = time.perf_counter()

    # Run both I/O operations concurrently.
    student_data, course_data = await asyncio.gather(
        get_student_data(),
        get_course_data()
    )

    end = time.perf_counter()

    return {
        "student_data": student_data,
        "course_data": course_data,
        "time_taken": round(end - start, 2)
    }