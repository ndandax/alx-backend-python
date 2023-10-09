#!/usr/bin/env python3
"""showing the functions of coroutine"""
import asyncio
import random
from typing import Optional
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int = 0) -> asyncio.Task:
    """Create an asyncio.Task by wrapping the wait_random coroutine"""
    return asyncio.ensure_future(wait_random(max_delay))
