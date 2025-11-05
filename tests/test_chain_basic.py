import types
import funcy as f
from funcy_pipe import funcy_extensions
from funcy_pipe.chain import Chain


def test_add_positive_numbers():
    numbers = [1, 2, 3]
    assert Chain(numbers).lmap(lambda x: x + 1) == [2, 3, 4]


def test_extension_patch():
    funcy_extensions.patch()
    assert isinstance(getattr(f, "where_not"), types.FunctionType)

    data = [{"a": 1}, {"a": 2}]
    result = Chain(data).where_not(a=2)
    assert result == [{"a": 1}]


def test_sort():
    funcy_extensions.patch()
    data = [{"s": 2, "b": True}, {"s": 1, "c": True}]
    result = Chain(data).sort(key="s")
    assert result == [{"s": 1, "c": True}, {"s": 2, "b": True}]


def test_join():
    funcy_extensions.patch()
    values = ["a", "b", "c"]
    result = Chain(values).join_str(", ")
    assert result == "a, b, c"


def test_compact():
    data = [1, 2, None, 3]
    assert Chain(list(data)).compact() == [1, 2, 3]

    compact_method = Chain(list(data)).compact
    assert compact_method() == [1, 2, 3]


def test_reject():
    funcy_extensions.patch()
    data = [1, 2, 3]
    result = Chain(data).reject(lambda x: x == 2)
    assert result == [1, 3]


def test_sample():
    funcy_extensions.patch()
    data = [1, 2, 3]
    result = Chain(data).sample().value_of()
    assert result in data


def test_chain_composition_matches_pipe():
    funcy_extensions.patch()
    data = [
        {"keep": True, "value": 1},
        {"keep": False, "value": 2},
        {"keep": True, "value": None},
        {"keep": True, "value": 3},
    ]

    chain = (
        Chain(data)
        .where_attr(keep=True)
        .pluck("value")
        .compact()
        .lmap(lambda x: x * 10)
    )

    assert chain == [10, 30]
