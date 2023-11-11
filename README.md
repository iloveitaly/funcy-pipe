# Funcy with pipeline-based operators

If [Funcy](https://github.com/Suor/funcy) and [Pipe](https://github.com/JulienPalard/Pipe) had a baby. Deal with data transformation in python in a sane way.

## Examples

```python
import funcy_pipe as f
entities_from_sql_alchemy
  | f.lmap(lambda r: r.to_dict())
  | f.lmap(lambda r: r | f.omit(["id", "created_at", "updated_at"]))
  | f.to_list
```

## Extras

* to_list
* log
* bp
* sort
* exactly_one
* reduce

### Module Alias

Create a module alias for `funcy-pipe` to make things clean (`import *` always irks me):

```python
# fp.py
from funcy_pipe import *

# code py
import fp
```

# Inspiration

* Elixir's pipe operator. `array |> map(fn) |> filter(fn)`
* Ruby's enumerable library. `array.map(&:fn).filter(&:fn)`
* https://pypi.org/project/funcy-chain
* https://github.com/JulienPalard/Pipe

# TODO

- [ ] tests
- [ ] relax python version
- [ ] fix typing threading
