#!/usr/bin/env python3
"""
Augment the following code with the correct duck-typed annotations:

"""

# The types of the elements of the input are not know

from typing import Union, List, Sequence, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
        Retrieve the first element of a sequence if it exists;
        otherwise, return None.

        This function takes a sequence (like a list or tuple) as input and
            returns the first element
        of the sequence if the sequence is non-empty. If the sequence is empty,
            it returns None.

            Args:
                lst (Sequence[Any]): A sequence containing elements
                    of any type.

            Returns:
                Union[Any, None]: The first element of the sequence
                if it exists; otherwise, None.

    """
    if lst:
        return lst[0]
    else:
        return None
