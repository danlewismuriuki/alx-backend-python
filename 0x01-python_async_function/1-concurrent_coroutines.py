#!/usr/bin/env python3
""" The basics of async """

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn wait_random n times with the specified max_delay and return a list
    of the delays in ascending order.

    Args:
        n (int): The number of times to spawn wait_random.
        max_delay (int): The maximum delay value to use with wait_random.

    Returns:
        List[float]: A list of delays in ascending order.
    """
    tasks = []

    # Create and collect tasks
    for _ in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        tasks.append(task)

    delays = []

    # Gather results as they complete
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    # Return sorted delays
    return sorted(delays)
