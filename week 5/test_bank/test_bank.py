from bank import value

def test_zero():
    assert value("hello")==0
    assert value("Hello")==0
    assert value("HELLO")==0

def test_twenty():
    assert value("hi")==20
    assert value("Hi")==20
    assert value("HI")==20

def test_hundred():
    assert value("What’s up")==100
    assert value("what hello")==100
