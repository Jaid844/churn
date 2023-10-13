# test_my_app.py

def add(a, b):
    return a + b

def test_add_positive_numbers():
    result = add(3, 5)
    assert result == 8

def test_add_negative_numbers():
    result = add(-2, -4)
    assert result == -6

def test_add_mixed_numbers():
    result = add(5, -3)
    assert result == 2
