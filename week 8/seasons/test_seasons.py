from seasons import convert

def test_convert():
    assert convert(1445)=="Two million, eighty thousand, eight hundred minutes"
    assert convert(365)=="Five hundred twenty-five thousand, six hundred minutes"
