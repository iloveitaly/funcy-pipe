import types
import funcy_pipe as fp
import funcy as f
from funcy_pipe import funcy_extensions
from funcy_pipe.pipe import PipeFirst, PipeSecond


def test_add_positive_numbers():
    assert [1, 2, 3] | fp.lmap(lambda x: x + 1) | fp.to_list == [2, 3, 4]


def test_extension_patch():
    funcy_extensions.patch()

    assert isinstance(f.where_not, types.FunctionType)


def test_sort():
    assert [{"s": 2, "b": True}, {"s": 1, "c": True}] | fp.sort(key="s") == [
        {"s": 1, "c": True},
        {"s": 2, "b": True},
    ]


def test_join():
    assert ["a", "b", "c"] | fp.join_str(", ") == "a, b, c"

def test_compact():
    """
    The sneaky truth here is if a function only has a single argument, it will be treated as a PipeFirst even if wrapped in a PipeSecond
    """

    assert isinstance(fp.compact, PipeFirst)

    assert [1, 2, None, 3] | fp.compact == [1, 2, 3]
    assert [1, 2, None, 3] | fp.compact() == [1, 2, 3]

def test_reject():
    assert [1, 2, 3] | fp.reject(lambda x: x == 2) | fp.to_list == [1, 3]

# TODO if the left object has a __or__ method, the right side __ror__ is ignored and you'll get a type error!
# def test_to_list_with_dict_items():
#     assert {"a": 1, "b": 2} | fp.iteritems() | fp.to_list() == [("a", 1), ("b", 2)]
