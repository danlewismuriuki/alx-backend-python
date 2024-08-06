Type Annotations for Generators in Python
This document provides an overview of type annotations for synchronous and asynchronous generators in Python. It covers how to use the typing module to specify the types of values yielded by generators, as well as the types of values they accept and return.

Table of Contents
Synchronous Generators
Asynchronous Generators
Examples
Usage
Synchronous Generators
Synchronous generators are functions that yield values one at a time, allowing iteration over a sequence of values.

Type Annotation
Use the Generator type from the typing module to type-annotate synchronous generators. The Generator type requires three type parameters:

Yield Type: The type of values the generator yields.
Send Type: The type of values that can be sent to the generator via the send() method (often None if not used).
Return Type: The type of value returned when the generator is exhausted (often None if not used).
Example:

python
Copy code
from typing import Generator

def count_up_to(max: int) -> Generator[int, None, None]:
    count = 1
    while count <= max:
        yield count
        count += 1
Asynchronous Generators
Asynchronous generators are used to produce values asynchronously, which is useful for handling I/O-bound tasks or large data streams.

Type Annotation
Use the AsyncGenerator type from the typing module to type-annotate asynchronous generators. The AsyncGenerator type requires three parameters:

Yield Type: The type of values the asynchronous generator yields.
Send Type: The type of values that can be sent to the asynchronous generator via the asend() method (often None if not used).
Return Type: The type of value returned when the asynchronous generator is exhausted (often None if not used).
Example:

python
Copy code
from typing import AsyncGenerator
import asyncio

async def async_count_up_to(max: int) -> AsyncGenerator[int, None]:
    count = 1
    while count <= max:
        await asyncio.sleep(1)
        yield count
        count += 1
Examples
Synchronous Generator Example
python
Copy code
from typing import Generator

def count_up_to(max: int) -> Generator[int, None, None]:
    count = 1
    while count <= max:
        yield count
        count += 1

for number in count_up_to(5):
    print(number)
Asynchronous Generator Example
python
Copy code
from typing import AsyncGenerator
import asyncio

async def async_count_up_to(max: int) -> AsyncGenerator[int, None]:
    count = 1
    while count <= max:
        await asyncio.sleep(1)
        yield count
        count += 1

async def main():
    async for number in async_count_up_to(5):
        print(number)

asyncio.run(main())
Usage
Type Annotate Generators: Use Generator for synchronous generators and AsyncGenerator for asynchronous generators.
Specify Types: Define the types for values yielded, values sent, and return values.
Implement: Use the annotated types to create generators and asynchronous generators that are clear and well-typed.
By following these practices, you can create more readable and type-safe code for generators in Python.


