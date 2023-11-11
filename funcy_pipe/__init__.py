from .pipe import PipeFirst, PipeSecond
import funcy

__all__ = []

# where the first param is the iterable
PIPE_FIRST_EXCEPTIONS = ["omit"]


def export(func):
    globals()["__all__"].append(func.__name__)
    return func


def apply_decorator_and_export(module, decorator):
    for name in dir(module):
        obj = getattr(module, name)
        if not callable(obj) or name.startswith("__"):
            continue

        decorated_fn = (
            PipeFirst(obj) if name in PIPE_FIRST_EXCEPTIONS else decorator(obj)
        )
        globals()[name] = decorated_fn
        __all__.append(name)


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


@PipeFirst
@export
def sort(iterable, key=None, reverse=False):
    # if key is str, assume it is a dict key
    if key is not None and type(key) is str:
        key = funcy.rpartial(funcy.get_in, [key])

    return sorted(iterable, key=key, reverse=reverse)


apply_decorator_and_export(funcy, PipeSecond)
