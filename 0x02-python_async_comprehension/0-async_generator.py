#!/usr/bin/env python3
"""coroutine called async_generator that takes no arguments. """
import asyncio
import random


async def async_generator() -> float:
    """coroutine will loop 10 times"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
