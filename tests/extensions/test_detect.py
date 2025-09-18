import funcy_pipe as fp


def test_detect_basic():
    """Test basic detect functionality with dicts"""
    data = [
        {'name': 'Alice', 'age': 25},
        {'name': 'Bob', 'age': 30},
        {'name': 'Charlie', 'age': 25}
    ]
    
    # Should find the first match
    result = data | fp.detect(age=25)
    assert result == {'name': 'Alice', 'age': 25}


def test_detect_multiple_conditions():
    """Test detect with multiple conditions"""
    data = [
        {'name': 'Alice', 'age': 25, 'city': 'NYC'},
        {'name': 'Bob', 'age': 30, 'city': 'SF'},
        {'name': 'Charlie', 'age': 25, 'city': 'NYC'}
    ]
    
    result = data | fp.detect(age=25, city='NYC')
    assert result == {'name': 'Alice', 'age': 25, 'city': 'NYC'}


def test_detect_no_match():
    """Test detect when no element matches"""
    data = [
        {'name': 'Alice', 'age': 25},
        {'name': 'Bob', 'age': 30}
    ]
    
    result = data | fp.detect(age=99)
    assert result is None


def test_detect_empty_list():
    """Test detect with empty list"""
    result = [] | fp.detect(name='Alice')
    assert result is None


def test_detect_attr_basic():
    """Test basic detect_attr functionality with objects"""
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age
            
        def __eq__(self, other):
            return self.name == other.name and self.age == other.age
    
    people = [
        Person('Alice', 25),
        Person('Bob', 30),
        Person('Charlie', 25)
    ]
    
    # Should find the first match
    result = people | fp.detect_attr(age=25)
    assert result == Person('Alice', 25)


def test_detect_attr_multiple_conditions():
    """Test detect_attr with multiple conditions"""
    class Person:
        def __init__(self, name, age, city):
            self.name = name
            self.age = age
            self.city = city
            
        def __eq__(self, other):
            return (self.name == other.name and 
                   self.age == other.age and 
                   self.city == other.city)
    
    people = [
        Person('Alice', 25, 'NYC'),
        Person('Bob', 30, 'SF'),
        Person('Charlie', 25, 'NYC')
    ]
    
    result = people | fp.detect_attr(age=25, city='NYC')
    assert result == Person('Alice', 25, 'NYC')


def test_detect_attr_no_match():
    """Test detect_attr when no object matches"""
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age
    
    people = [Person('Alice', 25), Person('Bob', 30)]
    
    result = people | fp.detect_attr(age=99)
    assert result is None


def test_detect_attr_missing_attribute():
    """Test detect_attr when object doesn't have the attribute"""
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age
    
    people = [Person('Alice', 25), Person('Bob', 30)]
    
    result = people | fp.detect_attr(height=180)  # height attribute doesn't exist
    assert result is None


def test_detect_attr_empty_list():
    """Test detect_attr with empty list"""
    result = [] | fp.detect_attr(name='Alice')
    assert result is None


def test_detect_equivalent_to_where_first():
    """Test that detect gives same result as where | first"""
    data = [
        {'name': 'Alice', 'age': 25},
        {'name': 'Bob', 'age': 30},
        {'name': 'Charlie', 'age': 25}
    ]
    
    # Both should give the same result
    result1 = data | fp.detect(age=25)
    result2 = data | fp.where(age=25) | fp.first()
    
    assert result1 == result2


def test_detect_attr_equivalent_to_where_attr_first():
    """Test that detect_attr gives same result as where_attr | first"""
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age
            
        def __eq__(self, other):
            return self.name == other.name and self.age == other.age
    
    people = [
        Person('Alice', 25),
        Person('Bob', 30),
        Person('Charlie', 25)
    ]
    
    # Both should give the same result
    result1 = people | fp.detect_attr(age=25)
    result2 = people | fp.where_attr(age=25) | fp.first()
    
    assert result1 == result2