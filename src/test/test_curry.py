from src.craftsmen import curry
from . import create_dummie_mock, mock_result, arg1, arg2, arg3

def test_mock_function():
    _dummie, _mock = create_dummie_mock()
    result = _dummie(arg1, arg2, arg3)
    assert result is mock_result
    _mock.assert_called_once_with(arg1, arg2, arg3)

def test_curry_natural_use():
    _dummie, _mock = create_dummie_mock()
    curry_function = curry(_dummie)
    result = curry_function(arg1, arg2, arg3)
    assert result is mock_result
    _mock.assert_called_once_with(arg1, arg2, arg3)

def test_curry_sequential_use():
    _dummie, _mock = create_dummie_mock()
    curry_function = curry(_dummie)
    partial = curry_function(arg1)
    partial = partial(arg2)
    result = partial(arg3)
    assert result is mock_result
    _mock.assert_called_once_with(arg1, arg2, arg3)

def test_curry_partial_sequential_use():
    _dummie, _mock = create_dummie_mock()
    curry_function = curry(_dummie)
    partial = curry_function(arg1)
    result = partial(arg2, arg3)
    assert result is mock_result
    _mock.assert_called_once_with(arg1, arg2, arg3)
