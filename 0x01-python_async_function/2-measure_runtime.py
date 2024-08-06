#!/usr/bin/env python3

""" The basics of async """

import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time of the wait_n coroutine and returns
    the average time per coroutine.

    Args:
    n (int): The number of coroutines to spawn and measure.
    max_delay (int): The maximum delay in seconds for each coroutine.

    Returns:
    float: The average time in seconds taken per coroutine call.

    The function uses the time module to record the start and end times
    of the wait_n coroutine execution and computes the average time per
    coroutine by dividing the total elapsed time by the number of coroutines.
    """

    start_time = time.time()

    asyncio.run(wait_n(n, max_delay))

    end_time = time.time()

    total_time = end_time - start_time

    return total_time / n
