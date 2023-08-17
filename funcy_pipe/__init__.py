from pipe import PipeFirst, PipeSecond
import funcy

__all__ = []

# where the first param is the iterable
PIPE_FIRST_EXCEPTIONS = ["omit"]


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
def to_list(iterable):
    return list(iterable)


# pipe-map: for use with `lmap` and similar
@PipeSecond
def pmap(func, iterable):
    return iterable | func


__all__.append("to_list")

apply_decorator_and_export(funcy, PipeSecond)
