import functools
import funcy

from .funcy_extensions import patch
from .pipe import PipeFirst, PipeSecond

__all__ = []

# where the first param is the iterable
PIPE_FIRST_EXCEPTIONS = ["omit", "iteritems", "itervalues", "empty"]
PIPE_FIRST_OMISSIONS = ["partial", "rpartial", "curry", "rcurry"]


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


# TODO there's `first` but it doesn't throw an exception if there's more than one
@export
def exactly_one(comprehension):
    # TODO detect if we are working with a generator/iterator and maybe use first?

    if len(comprehension) != 1:
        raise Exception("Expected to find exactly one matching item")

    return comprehension[0]


# TODO should document in funcy and remove this
# https://github.com/Suor/funcy/commit/bbc249672df3839fc0e3f3fc9fbb4483978886b5
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
