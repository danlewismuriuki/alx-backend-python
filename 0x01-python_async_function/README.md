# Async Programming and Random Module in Python

## Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

1. **Async and Await Syntax**
2. **How to Execute an Async Program with asyncio**
3. **How to Run Concurrent Coroutines**
4. **How to Create asyncio Tasks**
5. **How to Use the Random Module**

## 1. Async and Await Syntax

In Python, `async` and `await` are used to write asynchronous code. The `async` keyword is used to declare a function as asynchronous, allowing it to use the `await` keyword. The `await` keyword is used to pause the execution of an `async` function until the result of an awaited operation is available.

### Example:

```python
import asyncio

async def fetch_data():
    await asyncio.sleep(1)
    return "data"

async def main():
    result = await fetch_data()
    print(result)

asyncio.run(main())

