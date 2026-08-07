# funcy_pipe.funcy_extensions

## Functions

| [`where_not`](#funcy_pipe.funcy_extensions.where_not)(mappings, \*\*cond)          | Iterates over mappings containing all pairs not in cond.     |
|------------------------------------------------------------------------------------|--------------------------------------------------------------|
| [`where_not_attr`](#funcy_pipe.funcy_extensions.where_not_attr)(objects, \*\*cond) |                                                              |
| [`where_attr`](#funcy_pipe.funcy_extensions.where_attr)(objects, \*\*cond)         |                                                              |
| [`pluck`](#funcy_pipe.funcy_extensions.pluck)(key, mappings)                       | Iterates over values for key, or multiple keys, in mappings. |
| [`shuffled`](#funcy_pipe.funcy_extensions.shuffled)(seq)                           |                                                              |
| [`sample`](#funcy_pipe.funcy_extensions.sample)(seq)                               | Pick a random element from the array                         |
| [`join_str`](#funcy_pipe.funcy_extensions.join_str)(sep, seq)                      |                                                              |
| [`sort`](#funcy_pipe.funcy_extensions.sort)(iterable[, key, reverse])              |                                                              |
| [`reject`](#funcy_pipe.funcy_extensions.reject)(coll, pred)                        |                                                              |
| [`detect`](#funcy_pipe.funcy_extensions.detect)(mappings, \*\*cond)                | Find the first mapping containing all pairs in cond.         |
| [`detect_attr`](#funcy_pipe.funcy_extensions.detect_attr)(objects, \*\*cond)       | Find the first object having all attributes matching cond.   |
| [`dig`](#funcy_pipe.funcy_extensions.dig)(path, data, \*[, default])               | Dig into nested dict using dot-path string or list of keys.  |
| [`patch`](#funcy_pipe.funcy_extensions.patch)()                                    |                                                              |

## Module Contents

### funcy_pipe.funcy_extensions.where_not(mappings, \*\*cond)

Iterates over mappings containing all pairs not in cond.

### funcy_pipe.funcy_extensions.where_not_attr(objects, \*\*cond)

### funcy_pipe.funcy_extensions.where_attr(objects, \*\*cond)

### funcy_pipe.funcy_extensions.pluck(key, mappings)

Iterates over values for key, or multiple keys, in mappings.

### funcy_pipe.funcy_extensions.shuffled(seq)

### funcy_pipe.funcy_extensions.sample(seq)

Pick a random element from the array

### funcy_pipe.funcy_extensions.join_str(sep, seq)

### funcy_pipe.funcy_extensions.sort(iterable, key=None, reverse=False)

### funcy_pipe.funcy_extensions.reject(coll, pred: Callable)

### funcy_pipe.funcy_extensions.detect(mappings, \*\*cond)

Find the first mapping containing all pairs in cond.

### funcy_pipe.funcy_extensions.detect_attr(objects, \*\*cond)

Find the first object having all attributes matching cond.

### funcy_pipe.funcy_extensions.dig(path, data, , default=None)

Dig into nested dict using dot-path string or list of keys.
Raises KeyError/TypeError if path missing and no default.

```pycon
>>> dig('a.b', {'a': {'b': 1}})
1
>>> dig('a.b', {'a': {'b': 1}}, default=42)
1
>>> dig('a.x', {'a': {'b': 1}}, default=42)
42
>>> dig('a.x', {'a': {'b': 1}})
Traceback (most recent call last):
...
KeyError: 'x'
>>> dig(['a', 'b'], {'a': {'b': 1}})
1
```

### funcy_pipe.funcy_extensions.patch()
