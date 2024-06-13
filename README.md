[![Release Notes](https://img.shields.io/github/release/iloveitaly/funcy-pipe)](https://github.com/iloveitaly/funcy-pipe/releases) [![Downloads](https://static.pepy.tech/badge/funcy-pipe/month)](https://pepy.tech/project/funcy-pipe) [![Python Versions](https://img.shields.io/pypi/pyversions/funcy-pipe)](https://pypi.org/project/funcy-pipe) ![GitHub CI Status](https://github.com/iloveitaly/funcy-pipe/actions/workflows/build_and_publish.yml/badge.svg) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# Funcy with pipeline-based operators

If [Funcy](https://github.com/Suor/funcy) and [Pipe](https://github.com/JulienPalard/Pipe) had a baby. Deal with data transformation in python in a sane way.

I love Ruby. It's a great language and one of the things they got right was pipelined data transformation. Elixir got this
even more right with the explicit pipeline operator `|>`.

However, Python is the way of the future. As I worked more with Python, it was driving me nuts that the
data transformation options were not chainable.

This project fixes this pet peeve.

## Installation

```shell
pip install funcy-pipe
```

Or, if you are using poetry:

```shell
poetry add funcy-pipe
```

## Examples

Extract a couple key values from a sql alchemy model:

```python notest
import funcy_pipe as fp

entities_from_sql_alchemy
  | fp.lmap(lambda r: r.to_dict())
  | fp.lmap(lambda r: r | fp.omit(["id", "created_at", "updated_at"]))
  | fp.to_list
```

Or, you can be more fancy and use [whatever](https://github.com/Suor/whatever) and `pmap`:

```python notest
import funcy_pipe as f
import whatever as _

entities_from_sql_alchemy
  | fp.lmap(_.to_dict)
  | fp.pmap(fp.omit(["id", "created_at", "updated_at"]))
  | fp.to_list
```

Create a map from an array of objects, ensuring the key is always an `int`:

```python notest
section_map = api.get_sections() | fp.group_by(f.compose(int, that.id))
```

Grab the ID of a specific user:

```python notest
filter_user_id = (
  collaborator_map().values()
  | fp.where(email=target_user)
  | fp.pluck("id")
  | fp.first()
)
```

Get distinct values from a list (in this case, github events):

```python
events = [
  {
    "type": "PushEvent"
  },
  {
    "type": "CommentEvent"
  }
]

result = events | fp.pluck("type") | fp.distinct() | fp.to_list()

assert ["PushEvent", "CommentEvent"] == result
```

What if the objects are not dicts?

```python notest
filter_user_id = (
  collaborator_map().values()
  | fp.where_attr(email=target_user)
  | fp.pluck_attr("id")
  | fp.first()
)
```

How about creating a dict where each value is sorted:

```python notest
data
  # each element is a dict of city information, let's group by state
  | fp.group_by(itemgetter("state_name"))
  # now let's sort each value by population, which is stored as a string
  | fp.walk_values(
    f.partial(sorted, reverse=True, key=lambda c: int(c["population"])),
  )
```

A more complicated example ([lifted from this project](https://github.com/iloveitaly/todoist-digest/blob/2f893709da2cf3a0f715125053af705fc3adbc4c/run.py#L151-L166)):

```python notest
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
    # there is no `sort` in the funcy library, so we reexport the sort built-in so it's pipe-able
    | fp.sort(key="posted_at_date")
    # create a dictionary of task_id => [comments]
    | fp.group_by(lambda comment: comment["task_id"])
)
```

Want to grab the values of a list of dict keys?

```python
def add_field_name(input: dict, keys: list[str]) -> dict:
    return input | {
        "field_name": (
            keys
            # this is a sneaky trick: if we reference the objects method, when it's called it will contain a reference
            # to the object
            | fp.map(input.get)
            | fp.compact
            | fp.join_str("_")
        )
    }

result = [{ "category": "python", "header": "functional"}] | fp.map(fp.rpartial(add_field_name, ["category", "header"])) | fp.to_list
assert result == [{'category': 'python', 'header': 'functional', 'field_name': 'python_functional'}]
```

You can also easily test multiple conditions across API data ([extracted from this project](https://github.com/iloveitaly/github-overlord/blob/a3c0e5d0765b3748747e6721e602c0021be0c8e1/github_overlord/__init__.py#L66-L71))

```python no test
all_checks_successful = (
    last_commit.get_check_runs()
    | fp.pluck_attr("conclusion")
    # if you pass a set into `all` each element of the set is used to build a predicate
    # this condition tests if the "conclusion" attribute is either "success" or "skipped"
    | fp.all({"success", "skipped"})
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

## Extensions

There [are some functions](funcy_pipe/funcy_extensions.py) which are not yet merged upstream into funcy, and may never be. You can patch `funcy` to add them using:

```python
import funcy_pipe
funcy_pipe.patch()
```

## Coming From Ruby?

* uniq => distinct
* detect => `where(some="Condition") | first` or `where_attr(some="Condition") | first`

### Module Alias

Create a module alias for `funcy-pipe` to make things clean (`import *` always irks me):

```python notest
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
- [ ] fix typing threading
