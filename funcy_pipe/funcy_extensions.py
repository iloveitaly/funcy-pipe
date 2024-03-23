from operator import itemgetter

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


def patch():
    f.where_attr = where_attr
    f.where_not = where_not
    f.where_not_attr = where_not_attr
    f.pluck = pluck
