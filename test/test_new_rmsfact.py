import rmsfact


def test_new_rms_fact_returns_function():
    """The `_new_rmsfact()` function should return a function"""
    assert hasattr(rmsfact._new_rmsfact(), "__call__")


def test_rmsfact_is_function():
    """`rmsfact.rmsfact()` should be a function"""
    assert hasattr(rmsfact.rmsfact, "__call__")


def test_returns_string():
    """`rmsfact.rmsfact()` should return a string"""
    fact = rmsfact.rmsfact()
    assert isinstance(fact, str)
