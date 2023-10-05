#!/usr/bin/env python3
"""a module to define a function that returns a function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """multiplier function"""
    def multiplier_function(x: float) -> float:
        """callable function"""
        return x * multiplier
    return multiplier_function
