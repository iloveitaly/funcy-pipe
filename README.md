# Funcy with pipeline-based operators

If Funcy and Pipe had a baby.

## Examples

```python
import funcy_pipe as f
entities_from_sql_alchemy
  | f.lmap(lambda r: r.to_dict())
  | f.lmap(lambda r: r | f.omit(["id", "created_at", "updated_at"]))
  | f.to_list
```

### Module Alias

Create a module alias for `funcy-pipe` to easily import in your project:

```python
# f.py
from funcy_pipe import *
```

# Inspiration

* https://pypi.org/project/funcy-chain
* https://github.com/JulienPalard/Pipe
* Ruby's enumerable library
* Elixir's pipe operator

# TODO

- [ ] tests
- [ ] relax python version
