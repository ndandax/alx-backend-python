#!/usr/bin/env python3
"""showing the functions of coroutine"""
import asyncio
from random import uniform
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay:int) -> float:
    """wait_random co-routine"""
    tasks = [wait_random(max_delay) for i in range(n)]
    results = await asyncio.gather(*tasks)
    sorted_results = sorted(results)
    return sorted_results