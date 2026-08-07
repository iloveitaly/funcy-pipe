# funcy_pipe.pipe

Adapted from:

[https://github.com/JulienPalard/Pipe/blob/main/pipe.py](https://github.com/JulienPalard/Pipe/blob/main/pipe.py)

## Classes

| [`PipeFirst`](#funcy_pipe.pipe.PipeFirst)   | Takes the input into | and passes to the first argument of the function   |
|---------------------------------------------|---------------------------------------------------------------------------|
| [`PipeSecond`](#funcy_pipe.pipe.PipeSecond) | Represent a Pipeable Element:                                             |

## Module Contents

### *class* funcy_pipe.pipe.PipeFirst(function)

Takes the input into | and passes to the first argument of the function

Described as:
>>> first = PipeFirst(lambda iterable: next(iter(iterable)))

and used as:
>>> print([1, 2, 3] | first)
1

Or represent a Pipeable Function :
It’s a function returning a Pipe
Described as :
>>> select = PipeFirst(lambda iterable, pred: (pred(x) for x in iterable))

and used as:
>>> list([1, 2, 3] | select(lambda x: x \* 2))
[2, 4, 6]

#### function

### *class* funcy_pipe.pipe.PipeSecond(function)

Represent a Pipeable Element:
Described as:

```pycon
>>> first = PipeSecond(lambda pred, i: next(iter(i)))
```

and used as :
>>> [1, 2, 3] | first(lambda: True)
1

Or represent a Pipeable Function:
It’s a function returning a Pipe
Described as:
>>> select = PipeSecond(lambda pred, iterable: (pred(x) for x in iterable))

and used as:
>>> list([1, 2, 3] | select(lambda x: x \* 2))
[2, 4, 6]

#### function
