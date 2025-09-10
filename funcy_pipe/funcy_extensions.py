from operator import itemgetter
import random
from typing import Callable

import funcy as f
import funcy_pipe as fp
from funcy import none
from funcy_pipe.pipe import PipeFirst, PipeSecond


# https://github.com/Suor/funcy/pull/143
def where_not(mappings, **cond):
    """Iterates over mappings containing all pairs not in cond."""
    items = cond.items()
    match = lambda m: none(k in m and m[k] == v for k, v in items)
    return filter(match, mappings)


fp.where_not = PipeFirst(where_not)


def where_not_attr(objects, **cond):
    items = cond.items()
    match = lambda obj: none(hasattr(obj, k) and getattr(obj, k) == v for k, v in items)
    return filter(match, objects)


fp.where_not_attr = PipeFirst(where_not_attr)


# https://github.com/Suor/funcy/pull/140
def where_attr(objects, **cond):
    items = cond.items()
    match = lambda obj: all(hasattr(obj, k) and getattr(obj, k) == v for k, v in items)
    return filter(match, objects)


fp.where_attr = PipeFirst(where_attr)


# NOTE this replaces an existing method
# https://github.com/Suor/funcy/pull/142
def pluck(key, mappings):
    """Iterates over values for key, or multiple keys, in mappings."""
    if isinstance(key, (list, tuple)):
        return map(itemgetter(*key), mappings)
    else:
        return map(itemgetter(key), mappings)


fp.pluck = PipeSecond(pluck)


# https://github.com/Suor/funcy/pull/147
def shuffled(seq):
    new_seq = list(seq)
    random.shuffle(new_seq)
    return new_seq


fp.shuffled = PipeFirst(shuffled)


# TODO propose as funcy addition
def sample(seq):
    "Pick a random element from the array"
    return random.choice(seq)


fp.sample = PipeFirst(sample)


# TODO propose as funcy addition
def join_str(sep, seq):
    return sep.join(seq)


fp.join_str = PipeSecond(join_str)


# TODO propose as funcy addition
def sort(iterable, key=None, reverse=False):
    # TODO what about objects?
    # if key is str, assume it is a dict key
    if key is not None and type(key) is str:
        key = f.rpartial(f.get_in, [key])

    return sorted(iterable, key=key, reverse=reverse)


fp.sort = PipeFirst(sort)


def reject(coll, pred: Callable):
    # invert the predicate
    return filter(f.complement(pred), coll)


fp.reject = PipeFirst(reject)


def patch():
    def add_to_module(func):
        """
        What I'm trying to figure out here is the best way to add methods to the module in a way that the type system picks up on it :/
        """
        setattr(f, func.__name__, func)
        f.__all__.append(func.__name__)
        fp.__all__.append(func.__name__)

    list(f.map(add_to_module, [
        where_attr,
        where_not,
        where_not_attr,
        shuffled,
        pluck,
        join_str,
        sort,
        reject,
        sample,
    ]))
