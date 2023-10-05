#!/usr/bin/env python3
"""a module to define a function to return a tuple"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """returns tuple"""
    return (k, float(v*v))
