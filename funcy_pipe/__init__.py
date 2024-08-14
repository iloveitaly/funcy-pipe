import functools
import funcy

from .funcy_extensions import patch
from .pipe import PipeFirst, PipeSecond

__all__ = []

# where the first param is the iterable
PIPE_FIRST_EXCEPTIONS = ["omit", "iteritems", "itervalues", "empty", "compact"]
# do not wrap these with Pipe object
PIPE_FIRST_OMISSIONS = [
    "partial",
    "rpartial",
    "curry",
    "rcurry",
    "isnone",
    "notnone",
    "inc",
    "dec",
    "even",
    "complement",
    "get_in"
]

# hand crafted things that will never be piped
EXCLUSIONS = ["ContextDecorator", "ErrorRateExceeded", "LazyObject"]

def export(func):
    globals()["__all__"].append(func.__name__)
    return func


export(patch)


def apply_decorator_and_export(module):
    decorated_functions = {}

    for name in dir(module):
        if name.startswith("__"):
            continue

        obj = getattr(module, name)

        if name in EXCLUSIONS:
            continue

        if not callable(obj):
            continue

        if name in PIPE_FIRST_OMISSIONS:
            globals()[name] = obj
            __all__.append(name)
            continue

        decorated_functions[name] = (
            PipeFirst(obj)
            if name in PIPE_FIRST_EXCEPTIONS
            else PipeSecond(obj)
        )

        # add function to the module
        globals()[name] = decorated_functions[name]
        __all__.append(name)

    return decorated_functions


fp = apply_decorator_and_export(funcy)


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


@export
def pipe(func):
    """
    >>> def f(arr):
    ...     return arr[0]
    >>> ["a", "b", "c"] | pipe(f)
    'a'
    """
    return PipeFirst(func)


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
    >>> [{"key":1, "keep": 1}, {"key":2, "keep":2}, {"key":3, "keep":3}] | pmap(omit("key")) | to_list()
    [{'keep': 1}, {'keep': 2}, {'keep': 3}]
    """
    return iterable | fp["map"](lambda x: x | func)
