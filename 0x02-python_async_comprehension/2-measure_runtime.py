#!/usr/bin/env python3

""" Async Comprehensions """

import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:

    """
    Measure the total runtime for executing the async_comprehension
    coroutine four times in parallel.

    This function uses asyncio.gather to run four instances of the
    async_comprehension coroutine
    concurrently and calculates the total time taken for all four
    coroutines to complete.

    Returns:
        float: The total runtime in seconds, representing the time
        taken to execute all four
               instances of async_comprehension concurrently.
    """

    start_time = time.time()

    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    end_time = time.time()

    return end_time - start_time
