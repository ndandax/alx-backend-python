#!/usr/bin/env python3
"""showing the functions of coroutine"""
import asyncio
import random


async def wait_random(max_delay: int = 0) -> float:
    """a function that shows coroutine"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
