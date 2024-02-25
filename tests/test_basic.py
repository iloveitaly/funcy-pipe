import types
import funcy_pipe as fp
import funcy as f
from funcy_pipe import funcy_extensions


def test_add_positive_numbers():
    assert [1, 2, 3] | fp.lmap(lambda x: x + 1) | fp.to_list == [2, 3, 4]


def test_extension_patch():
    funcy_extensions.patch()

    assert isinstance(f.where_not, types.FunctionType)
