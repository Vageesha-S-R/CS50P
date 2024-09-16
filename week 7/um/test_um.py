from um import count

def test_count():
    assert count("hello, um, world")==1
    assert count("yummy")==0
    assert count("um")==1
    assert count("Um?")==1
    assert count("um, thanks, um...")==2
