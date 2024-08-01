#!/usr/bin/env python3
"""
More involved type annotations
Add type annotations to function safely_get_value
"""
from typing import Mapping, Union, TypeVar, Any

# Define a TypeVar to represent the type of the default value
T = TypeVar('T')


def safely_get_value(dct: Mapping[Any, T], key: Any, default:
                     Union[T, None] = None) -> Union[T, None]:
    """
    Safely retrieves a value from a dictionary or returns a default value.

    Args:
        dct (Mapping[Any, T]): The dictionary from which to retrieve the value.
        key (Any): The key to look up in the dictionary.
        default (Union[T, None]): default value to return if key not found.

    Returns:
        Union[T, None]: The value associated with the key or the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
