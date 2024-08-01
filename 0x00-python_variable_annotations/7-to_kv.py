#!/usr/bin/env python3
"""
    function to_kv that takes a string k and an int OR float v as arguments
    returns a tuple. The first element of the tuple is the string k.
    The second element is the square of the int/float v and
    should be annotated as a float.
"""
from typing import List, Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
        parameters:
            k: A string (str).
            v: Can be either an integer (int) or a float (float).
        Return Type:
            Tuple[str, float]: A tuple where the first element is a string
                the second element is a float.
    """

    return (k, (v * v))
