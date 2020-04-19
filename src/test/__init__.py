import mock
from unittest.mock import create_autospec

class fake_value():
    pass

mock_result = fake_value()
arg1 = fake_value()
arg2 = fake_value()
arg3 = fake_value()

def create_dummie_mock():
    def _mock_function(a, b, c):
        return _mock(a, b, c)

    _mock = create_autospec(_mock_function, return_value=mock_result)

    def _dummie(a, b, c):
        return _mock(a, b, c)

    return _dummie, _mock
