from main import average, calculate_max, calculate_min, outliers, is_valid_value

def test_average():
    assert average([12, 0, 32, 40, 28, 38]) == 25, "average should be 25"
    assert average([]) == None
    assert average([20, 20, 20, 20, 20, 20]) == 20

def test_calculate_max():
    assert calculate_max([12, 0, 32, 40, 28, 38]) == 40, "maximum should be 40"
    assert calculate_max([18]) == 18
    assert calculate_max([19, 19, 19, 19]) == 19 
    assert calculate_max([-5, -10, -3]) == -3

def test_calculate_min():
    assert calculate_min([12, 0, 32, 40, 28, 38]) == 0, "minimum should be 0"
    assert calculate_min([18]) == 18
    assert calculate_min([19, 19, 19, 19]) == 19 
    assert calculate_min([-5, -10, -3]) == -10

def test_outliers():
    assert outliers([12, 0, 32, 40, 28, 38], 10) == [12, 0, 40, 38]
    assert outliers([12, 0, 32, 40, 28, 38], 0) == [12, 0, 32, 40, 28, 38]
    assert outliers([5, 10, 15, 25, 40], 25) == []

def test_is_valid_value():
    assert is_valid_value(0) == True, "0 should be a valid value"
    assert is_valid_value(40) == True, "40 should be a valid value"
    assert is_valid_value(-1) == False, "-1 should be an invalid value"
    assert is_valid_value(41) == False, "41 should be an invalid value"