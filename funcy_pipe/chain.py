"""
TODO not ready for prime time
Chain(a).map(lambda n: n + 1).filter(lambda n: n>2).list()
"""

import funcy
import funcy_pipe as fp_module

from collections.abc import Iterator

from .constants import PIPE_FIRST_EXCEPTIONS, PIPE_FIRST_OMISSIONS
from .pipe import PipeFirst, PipeSecond

# TODO autogen types for this too.
# TODO need list, set, etc methods for this


class Chain:
    def __init__(self, value):
        self.value = value

    @staticmethod
    def _wrap_result(value):
        if isinstance(value, Iterator):
            return list(value)

        return value

    def __iter__(self):
        return iter(self.value)

    def __len__(self):
        return len(self.value)

    def __eq__(self, other):
        if isinstance(other, Chain):
            return self.value == other.value
        return self.value == other

    def value_of(self):
        return self.value

    def list(self):
        return list(self.value)

    def __repr__(self):
        return f"Chain({self.value!r})"

    def __getattr__(self, name):
        "forward method calls to the associated method"

        attr = getattr(fp_module, name, None)

        if isinstance(attr, (PipeFirst, PipeSecond)):

            def pipe_method(*args, **kwargs):
                pipe_callable = attr if not (args or kwargs) else attr(*args, **kwargs)
                result = self.value | pipe_callable
                return Chain(self._wrap_result(result))

            return pipe_method

        if callable(attr) and name in PIPE_FIRST_OMISSIONS:
            return attr

        attr = getattr(funcy, name, None)

        if callable(attr):
            if name in PIPE_FIRST_EXCEPTIONS:

                def first_method(*args, **kwargs):
                    result = attr(self.value, *args, **kwargs)
                    return Chain(self._wrap_result(result))

                return first_method

            def second_method(*args, **kwargs):
                result = attr(*args, self.value, **kwargs)
                return Chain(self._wrap_result(result))

            return second_method

        raise AttributeError(
            f"'{self.__class__.__name__}' object has no attribute '{name}'"
        )


# Usage:
# f = Forwarder()
# f.some_method_from_some_module(args)

# Chain(a).map(lambda n: n + 1).filter(lambda n: n>2).list()
