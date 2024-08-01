#!/usr/bin/env python3

"""
    Annotate function’s parameters
    return values with the appropriate types
"""
from typing import Sequence, Tuple, List, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
        Annotate function’s parameters
        return values with the appropriate types
    """
    return [(i, len(i)) for i in lst]
