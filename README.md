# Funcy with pipeline-based operators

If [Funcy](https://github.com/Suor/funcy) and [Pipe](https://github.com/JulienPalard/Pipe) had a baby. Deal with data transformation in python in a sane way.

## Examples

```python
import funcy_pipe as f
entities_from_sql_alchemy
  | fp.lmap(lambda r: r.to_dict())
  | fp.lmap(lambda r: r | fp.omit(["id", "created_at", "updated_at"]))
  | fp.to_list
```

Or, you can be more fancy and use [whatever](https://github.com/Suor/whatever) and `pmap`:

```python
import funcy_pipe as f
entities_from_sql_alchemy
  | fp.lmap(_.to_dict)
  | fp.pmap(fp.omit(["id", "created_at", "updated_at"]))
  | fp.to_list
```

A more complicated example ([lifted from this project](https://github.com/iloveitaly/todoist-digest/blob/2f893709da2cf3a0f715125053af705fc3adbc4c/run.py#L151-L166)):

```python
comments = (
    # tasks are pulled from the todoist api
    tasks
    # get all comments for each relevant task
    | fp.lmap(lambda task: api.get_comments(task_id=task.id))
    # each task's comments are returned as an array, let's flatten this
    | fp.flatten()
    # dates are returned as strings, let's convert them to datetime objects
    | fp.lmap(enrich_date)
    # no date filter is applied by default, we don't want all comments
    | fp.lfilter(lambda comment: comment["posted_at_date"] > last_synced_date)
    # comments do not come with who created the comment by default, we need to hit a separate API to add this to the comment
    | fp.lmap(enrich_comment)
    # only select the comments posted by our target user
    | fp.lfilter(lambda comment: comment["posted_by_user_id"] == filter_user_id)
    | fp.sort(key="posted_at_date")
    # create a dictionary of task_id => [comments]
    | fp.group_by(lambda comment: comment["task_id"])
)
```

## Extras

* to_list
* log
* bp
* sort
* exactly_one
* reduce
* pmap

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
- [ ] docs for additional utils
- [ ] relax python version
- [ ] fix typing threading
