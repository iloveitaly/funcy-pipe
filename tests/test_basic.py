import pytest
import funcy_pipe as f

def test_add_positive_numbers():
    assert [1,2,3] | f.lmap(lambda x: x + 1) | f.to_list == [2,3,4]
