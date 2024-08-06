#!/usr/bin/env python3

"""
    function task_wait_random that takes an integer max_delay
    returns asyncio.Task.
"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay) -> asyncio.Task:
    """
    Create and return an asyncio.Task to run the wait_random coroutine.

    Args:
    max_delay (int): The maximum delay in seconds for the wait_random
    coroutine.

    Returns;
    asyncio.Task: A Task object that represents the wait_random coroutine.
    """
    return asyncio.create_task(wait_random(max_delay))
