#!/usr/bin/env python3
"""a module to show duck-typing annotations"""
from typing import Iterable, Union, Any


def safe_first_element(lst: Iterable) -> Union[None, Any]:
    """duck typing"""
    if lst:
        return next(iter(lst), None)
    else:
        return None
