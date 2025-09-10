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

def test_sample():
    assert [1, 2, 3] | fp.sample() in [1, 2, 3]


def test_sample_with_generator():
    """Test sample function with generator objects"""
    def gen():
        yield 1
        yield 2  
        yield 3
    
    result = gen() | fp.sample()
    assert result in [1, 2, 3]


def test_sample_with_filter():
    """Test sample function with filter objects"""
    result = filter(lambda x: x > 1, [1, 2, 3, 4]) | fp.sample()
    assert result in [2, 3, 4]


def test_sample_with_map():
    """Test sample function with map objects"""
    result = map(lambda x: x * 2, [1, 2, 3]) | fp.sample()
    assert result in [2, 4, 6]


def test_sample_with_tuple():
    """Test sample function with tuples (should use original path)"""
    result = (10, 20, 30) | fp.sample()
    assert result in [10, 20, 30]


def test_sample_with_string():
    """Test sample function with strings (should use original path)"""
    result = "xyz" | fp.sample()
    assert result in ['x', 'y', 'z']


def test_sample_empty_generator():
    """Test sample function with empty generator should raise IndexError"""
    def empty_gen():
        return
        yield  # This will never execute
    
    try:
        empty_gen() | fp.sample()
        assert False, "Expected IndexError for empty generator"
    except IndexError:
        pass  # This is expected behavior


def test_sample_empty_filter():
    """Test sample function with empty filter should raise IndexError"""
    try:
        filter(lambda x: x > 10, [1, 2, 3]) | fp.sample()
        assert False, "Expected IndexError for empty filter"
    except IndexError:
        pass  # This is expected behavior

# TODO if the left object has a __or__ method, the right side __ror__ is ignored and you'll get a type error!
# def test_to_list_with_dict_items():
#     assert {"a": 1, "b": 2} | fp.iteritems() | fp.to_list() == [("a", 1), ("b", 2)]
