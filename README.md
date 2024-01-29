# Funcy with pipeline-based operators

If [Funcy](https://github.com/Suor/funcy) and [Pipe](https://github.com/JulienPalard/Pipe) had a baby. Deal with data transformation in python in a sane way.

I love Ruby, but believe Python is the way of the future. As I worked more with Python, it was driving me nuts that the
data transformation options were not chainable like Ruby + Elixir. This project fixes this pet peeve.

## Examples

Extract a couple key values from a sql alchemy model:

```python
import funcy_pipe as fp

entities_from_sql_alchemy
  | fp.lmap(lambda r: r.to_dict())
  | fp.lmap(lambda r: r | fp.omit(["id", "created_at", "updated_at"]))
  | fp.to_list
```

Or, you can be more fancy and use [whatever](https://github.com/Suor/whatever) and `pmap`:

```python
import funcy_pipe as f
import whatever as _

entities_from_sql_alchemy
  | fp.lmap(_.to_dict)
  | fp.pmap(fp.omit(["id", "created_at", "updated_at"]))
  | fp.to_list
```

Create a map from an array of objects, ensuring the key is always an `int`:

```python
section_map = api.get_sections() | fp.group_by(f.compose(int, that.id))
```

Grab the ID of a specific user:

```python
filter_user_id = (
  collaborator_map().values()
  | fp.where(email=target_user)
  | fp.pluck("id")
  | fp.first()
)
```

What if the objects are not dicts?

```python
filter_user_id = (
  collaborator_map().values()
  | fp.where_attr(email=target_user)
  | fp.pluck_attr("id")
  | fp.first()
)
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
* bp. run `breakpoint()` on the input value
* sort
* exactly_one. Throw an error if the input is not exactly one element
* reduce
* pmap. Pass each element of a sequence into a pipe'd function

## Coming From Ruby?

* uniq => distinct
* detect => `where(some="Condition") | first` or `where_attr(some="Condition") | first`

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
