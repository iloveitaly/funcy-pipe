import funcy_pipe as fp
import funcy as f
from funcy_pipe import funcy_extensions


def test_min_basic():
    """Test basic min functionality."""
    assert [1, 2, 3] | fp.min() == 1
    assert [3, 1, 2] | fp.min() == 1
    assert [-1, -2, -3] | fp.min() == -3


def test_min_with_single_additional():
    """Test min with single additional value."""
    assert [1, 2, 3] | fp.min(0) == 0
    assert [1, 2, 3] | fp.min(5) == 1
    assert [5, 6, 7] | fp.min(1) == 1


def test_min_with_list_additional():
    """Test min with list of additional values."""
    assert [1, 2, 3] | fp.min([0, 4]) == 0
    assert [1, 2, 3] | fp.min([5, 6]) == 1
    assert [5, 6, 7] | fp.min([1, 8]) == 1


def test_max_basic():
    """Test basic max functionality."""
    assert [1, 2, 3] | fp.max() == 3
    assert [3, 1, 2] | fp.max() == 3
    assert [-1, -2, -3] | fp.max() == -1


def test_max_with_single_additional():
    """Test max with single additional value."""
    assert [1, 2, 3] | fp.max(5) == 5
    assert [1, 2, 3] | fp.max(0) == 3
    assert [5, 6, 7] | fp.max(10) == 10


def test_max_with_list_additional():
    """Test max with list of additional values."""
    assert [1, 2, 3] | fp.max([5, 4]) == 5
    assert [1, 2, 3] | fp.max([0, -1]) == 3
    assert [5, 6, 7] | fp.max([8, 10]) == 10


def test_sum_basic():
    """Test basic sum functionality."""
    assert [1, 2, 3] | fp.sum() == 6
    assert [0, 1, 2] | fp.sum() == 3
    assert [] | fp.sum() == 0


def test_sum_with_start():
    """Test sum with start value."""
    assert [1, 2, 3] | fp.sum(10) == 16
    assert [0, 1, 2] | fp.sum(5) == 8
    assert [] | fp.sum(10) == 10


def test_aggregates_patched():
    """Test that aggregate functions are properly patched into funcy module with correct names."""
    funcy_extensions.patch()
    
    # Test that the functions exist in funcy after patching with correct names
    assert hasattr(f, 'min')
    assert hasattr(f, 'max') 
    assert hasattr(f, 'sum')
    
    # Test that they work through funcy
    assert f.min([1, 2, 3]) == 1
    assert f.max([1, 2, 3]) == 3
    assert f.sum([1, 2, 3]) == 6