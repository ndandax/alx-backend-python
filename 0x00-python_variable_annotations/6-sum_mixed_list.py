#!/usr/bin/env python3
"""a module to define a function that uses multiple types"""
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """returns float from complex list addition"""
    return sum(mxd_lst)
