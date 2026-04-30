from hello import greet

def test_greet_default():
    """Test default greeting"""
    assert greet() == "Hello, World!"

def test_greet_with_name():
    """Test greeting with a name"""
    assert greet("Buildkite") == "Hello, Buildkite!"

def test_greet_returns_string():
    """Test return type"""
    result = greet("Test")
    assert isinstance(result, str)
