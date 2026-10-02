import asyncio
import time


async def task1():
    for i in range(3):
        print(f"Task 1 iterated : {i} and going to sleep")
        await asyncio.sleep(3)
    print("TASK 1 FULLY COMPLETED")


async def task2():
    for i in range(3):
        print(f"Task 2 iterated : {i} and going to sleep")
        await asyncio.sleep(3)
    print("TASK 2 FULLY COMPLETED")


async def task3():
    for i in range(3):
        print(f"Task 3 iterated : {i} and going to sleep")
    print("TASK 3 FULLY COMPLETED")


async def main():
    start_time = time.time()
    await asyncio.gather(task1(), task2(), task3())
    end_time = time.time()
    print(f"\nAll tasks completed in {end_time - start_time} seconds")


if __name__ == "__main__":
    asyncio.run(main())
