#!/usr/bin/env python3
"""showing the functions of coroutine"""
import asyncio
import time
from typing import List
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """couroutine to measure time"""
    start_time = time.time()
    tasks: List[asyncio.Task] = [wait_n(n, max_delay) for _ in range(n)]
    await asyncio.gather(*tasks)

    end_time = time.time()
    total_time = end_time - start_time
    average_time = total_time / n
    return average_time
