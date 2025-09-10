import funcy_pipe as fp


def test_sample_basic():
    """Test basic sample functionality with list"""
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