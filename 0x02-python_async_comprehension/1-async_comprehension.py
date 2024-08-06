#!/usr/bin/env python3

""""
Import async_generator from the previous task
Write a coroutine called async_comprehension that takes no arguments.

The coroutine will collect 10 random numbers using an async comprehensing
over async_generator, then return the 10 random numbers

"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers using asynchronous comprehension over
    async_generator.

    Returns:
        List[float]: A list of 10 random float numbers.
    """
    return [x async for x in async_generator()]
