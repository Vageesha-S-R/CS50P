from working import convert
import pytest


def test_Format():
    with pytest.raises(ValueError):
        convert("9 AM - 9 PM")

def test_hour():
    with pytest.raises(ValueError):
        convert("17 AM to 13 PM")

def test_min():
    with pytest.raises(ValueError):
        convert("9:60 AM to 9:60 PM")

def test_time():
    assert convert("10:30 PM to 8 AM")=="22:30 to 08:00"
    assert convert("9 AM to 5 PM")=="09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM")=="09:00 to 17:00"

