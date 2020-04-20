from src.craftsmen import cmap, p

arg_list = [1, 2, 3, 4, 5, 6, 7]
expected_result  = [2, 4, 6, 8, 10, 12, 14]

double_function = lambda a: a * 2
original_map = lambda val: map(double_function, val)

def test_original_function():
    result = original_map(arg_list)
    assert list(result) == expected_result

def test_map_natural_use():
    result = cmap(double_function, arg_list)
    assert list(result) == expected_result

def test_map_sequential_use():
    double_map = cmap(double_function)
    result = double_map(arg_list)
    assert list(result) == expected_result

def test_map_with_placeholder():
    args_map = cmap(p, arg_list)
    result = args_map(double_function)
    assert list(result) == expected_result
