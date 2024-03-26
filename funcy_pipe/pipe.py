# https://github.com/JulienPalard/Pipe/blob/main/pipe.py
import functools


class PipeFirst:
    """
    Takes the input into `|` and passes to the first argument of the function

    Described as:
    >>> first = Pipe(lambda iterable: next(iter(iterable)))
    and used as:
    >>> print([1, 2, 3] | first)
    1

    Or represent a Pipeable Function :
    It's a function returning a Pipe
    Described as :
    >>> select = Pipe(lambda iterable, pred: (pred(x) for x in iterable))
    and used as:
    >>> print([1, 2, 3] | select(lambda x: x * 2))
    2, 4, 6
    """

    def __init__(self, function):
        self.function = function
        functools.update_wrapper(self, function)

    def __ror__(self, other):
        return self.function(other)

    def __call__(self, *args, **kwargs):
        return PipeFirst(
            lambda iterable, *args2, **kwargs2: self.function(
                iterable, *args, *args2, **kwargs, **kwargs2
            )
        )


class PipeSecond:
    """
    Represent a Pipeable Element :
    Described as :
    first = Pipe(lambda iterable: next(iter(iterable)))
    and used as :
    print [1, 2, 3] | first
    printing 1

    Or represent a Pipeable Function :
    It's a function returning a Pipe
    Described as :
    select = Pipe(lambda iterable, pred: (pred(x) for x in iterable))
    and used as :
    print [1, 2, 3] | select(lambda x: x * 2)
    # 2, 4, 6
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
