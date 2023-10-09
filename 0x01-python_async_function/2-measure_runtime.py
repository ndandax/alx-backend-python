#!/usr/bin/env python3
"""showing the functions of coroutine"""
import asyncio
import time
from typing import List
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: float) -> float:
    """couroutine to measure time"""
    start_time = time.time()
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    delays: List[float] = loop.run_until_complete(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    average_time = total_time / n
    return average_time
