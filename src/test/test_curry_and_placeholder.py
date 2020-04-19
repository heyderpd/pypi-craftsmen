from src.craftsmen import curry, p
from src.test import create_dummie_mock, mock_result, arg1, arg2, arg3

def test_curry_with_none_placeholder():
    _dummie, _mock = create_dummie_mock()
    curry_function = curry(_dummie)
    partial = curry_function(arg1)
    partial = partial(arg2)
    result = partial(arg3)
    assert result is mock_result
    _mock.assert_called_once_with(arg1, arg2, arg3)

def test_curry_with_one_placeholder():
    _dummie, _mock = create_dummie_mock()
    curry_function = curry(_dummie)
    partial = curry_function(p, p, arg3)
    partial = partial(arg1)
    result = partial(arg2)
    assert result is mock_result
    _mock.assert_called_once_with(arg1, arg2, arg3)

def test_curry_with_two_placeholder():
    _dummie, _mock = create_dummie_mock()
    curry_function = curry(_dummie)
    partial = curry_function(p, arg2, arg3)
    result = partial(arg1)
    assert result is mock_result
    _mock.assert_called_once_with(arg1, arg2, arg3)

def test_curry_with_midle_placeholder():
    _dummie, _mock = create_dummie_mock()
    curry_function = curry(_dummie)
    partial = curry_function(p, arg2, p)
    partial = partial(arg1)
    result = partial(arg3)
    assert result is mock_result
    _mock.assert_called_once_with(arg1, arg2, arg3)

def test_curry_with_partial_placeholder():
    _dummie, _mock = create_dummie_mock()
    curry_function = curry(_dummie)
    partial = curry_function(p, arg2)
    partial = partial(arg1)
    result = partial(arg3)
    assert result is mock_result
    _mock.assert_called_once_with(arg1, arg2, arg3)

def test_curry_with_full_placeholder():
    _dummie, _mock = create_dummie_mock()
    curry_function = curry(_dummie)
    partial = curry_function(p, p, p)
    partial = partial(arg1)
    partial = partial(arg2)
    result = partial(arg3)
    assert result is mock_result
    _mock.assert_called_once_with(arg1, arg2, arg3)
