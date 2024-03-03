from calendar import c
import functools
import random
import funcy

from .funcy_extensions import patch
from .pipe import PipeFirst, PipeSecond

__all__ = []

# where the first param is the iterable
PIPE_FIRST_EXCEPTIONS = ["omit"]
PIPE_FIRST_OMISSIONS = ["partial"]


def export(func):
    globals()["__all__"].append(func.__name__)
    return func


export(patch)


def apply_decorator_and_export(module, decorator):
    decorated_functions = {}

    for name in dir(module):
        if name.startswith("__"):
            continue

        obj = getattr(module, name)

        if not callable(obj):
            continue

        if name in PIPE_FIRST_OMISSIONS:
            globals()[name] = obj
            __all__.append(name)
            continue

        decorated_functions[name] = (
            # TODO lol why pass in decorator if this logic exists?
            PipeFirst(obj)
            if name in PIPE_FIRST_EXCEPTIONS
            else decorator(obj)
        )

        # add function to the module
        globals()[name] = decorated_functions[name]
        __all__.append(name)

    return decorated_functions


fp = apply_decorator_and_export(funcy, PipeSecond)


@PipeFirst
@export
def to_list(iterable):
    return list(iterable)


@PipeFirst
@export
def log(iterable):
    # TODO maybe use pretty print
    print(iterable)
    return iterable


# breakpoint, avoid collision with built-in breakpoint
@PipeFirst
@export
def bp(iterable):
    breakpoint()
    return iterable


# https://github.com/Suor/funcy/pull/143
@PipeFirst
@export
def where_not(mappings, **cond):
    """Iterates over mappings containing all pairs not in cond."""
    items = cond.items()
    match = lambda m: none(k in m and m[k] == v for k, v in items)
    return filter(match, mappings)


# https://github.com/Suor/funcy/pull
@PipeFirst
@export
def shuffle(seq):
    new_seq = seq.copy()
    random.shuffle(new_seq)
    return new_seq


@PipeFirst
@export
def sort(iterable, key=None, reverse=False):
    # if key is str, assume it is a dict key
    if key is not None and type(key) is str:
        key = funcy.rpartial(funcy.get_in, [key])

    return sorted(iterable, key=key, reverse=reverse)


# TODO there's `first` but it doesn't throw an exception if there's more than one
@export
def exactly_one(comprehension):
    # TODO detect if we are working with a generator/iterator and maybe use first?

    if len(comprehension) != 1:
        raise Exception("Expected to find exactly one matching item")

    return comprehension[0]


@PipeFirst
@export
def reduce(iterable, func, initial):
    return functools.reduce(func, iterable, initial)


@PipeFirst
@export
def pmap(iterable, func):
    """
    >>> [1, 2, 3] | fp.pmap(fp.omit("key"))
    """
    return iterable | fp["map"](lambda x: x | func)
