from plates import is_valid

def test_len():
    assert is_valid("HELLO")==True
    assert is_valid("HELLO, WORLD")==False
    assert is_valid("GOODBYE")==False

def test_alnum():
    assert is_valid("CS50")==True
    assert is_valid("CS50!")==False

def test_digit():
    assert is_valid("CS05")==False
    assert is_valid("05CS")==False
    assert is_valid("C5")==False
    assert is_valid("50")==False

def test_alpha():
    assert is_valid("CS50CS")==False
