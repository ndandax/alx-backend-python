#!/usr/bin/env python3
"""coroutine called async_generator that takes no arguments. """
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """running a coroutine 4 times"""
    start_time = asyncio.get_event_loop().time()
    task = async_comprehension()
    await asyncio.gather(task, task, task, task)
    end_time = asyncio.get_event_loop().time()
    total = end_time - start_time
    return total
