from twttr import shorten

def test_lower():
    assert shorten("vageesha")=="vgsh"
    assert shorten("hello world!!")=="hll wrld!!"
    assert shorten("vagee123")=="vg123"
def test_upper():
    assert shorten("VAGEESHA")=="VGSH"
    assert shorten("HELLO WORLD!!")=="HLL WRLD!!"
