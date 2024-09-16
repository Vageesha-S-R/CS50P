from fuel import convert,gauge
import pytest

def test_convert():
    assert convert("3/4")==75
    assert convert("1/2")==50
    assert convert("1/100")==1

def test_gauge():
    assert gauge(1)=="E"
    assert gauge(99)=="F"
    assert gauge(75)==f"{75}%"

def test_Value():
    with pytest.raises(ValueError):
        convert("4/3")

def test_Zero():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
