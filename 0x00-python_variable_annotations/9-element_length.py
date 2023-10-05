#!/usr/bin/env python3
"""a module to define a function that uses iterables"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """using iterables"""
    return [(i, len(i)) for i in lst]
