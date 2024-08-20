"""
Adapted from:

https://github.com/JulienPalard/Pipe/blob/main/pipe.py
"""

import functools


class PipeFirst:
    """
    Takes the input into `|` and passes to the first argument of the function

    Described as:
    >>> first = PipeFirst(lambda iterable: next(iter(iterable)))

    and used as:
    >>> print([1, 2, 3] | first)
    1

    Or represent a Pipeable Function :
    It's a function returning a Pipe
    Described as :
    >>> select = PipeFirst(lambda iterable, pred: (pred(x) for x in iterable))

    and used as:
    >>> list([1, 2, 3] | select(lambda x: x * 2))
    [2, 4, 6]
    """

    def __init__(self, function):
        self.function = function
        functools.update_wrapper(self, function)

    def __ror__(self, other):
        return self.function(other)

    def __call__(self, *args, **kwargs):
        # this is called when the function is wrapped

        return PipeFirst(
            # pass the argument collected from __ror__ to the first argument of the function
            lambda iterable, *args2, **kwargs2: self.function(
                # args & kwargs are empty here in our case
                iterable, *args, *args2, **kwargs, **kwargs2
            )
        )

    def __repr__(self):
        # Customize the representation to include the function name
        return f"<PipeFirst wrapping {self.__name__} at {hex(id(self))}>"


class PipeSecond:
    """
    Represent a Pipeable Element:
    Described as:

    >>> first = PipeSecond(lambda pred, i: next(iter(i)))

    and used as :
    >>> [1, 2, 3] | first(lambda: True)
    1

    Or represent a Pipeable Function:
    It's a function returning a Pipe
    Described as:
    >>> select = PipeSecond(lambda pred, iterable: (pred(x) for x in iterable))

    and used as:
    >>> list([1, 2, 3] | select(lambda x: x * 2))
    [2, 4, 6]
    """

    def __init__(self, function):
        self.function = function
        functools.update_wrapper(self, function)

    def __ror__(self, other):
        return self.function(other)

    def __call__(self, *args, **kwargs):
        return PipeSecond(
            lambda iterable, *args2, **kwargs2: self.function(
                *args, *args2, iterable, **kwargs, **kwargs2
            )
        )

    def __repr__(self):
        # Customize the representation to include the function name
        return f"<PipeSecond wrapping {self.__name__} at {hex(id(self))}>"
