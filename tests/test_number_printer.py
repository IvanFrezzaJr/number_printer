import pytest
from number_printer import cli

def test_multiplesThree():
    assert True == cli._multiplesThree(3)
    assert False == cli._multiplesThree(5)
    with pytest.raises(TypeError):
        cli._multiplesThree("")
        cli._multiplesThree(None)

def test_multiplesFive():
    assert True == cli._multiplesFive(5)
    assert False == cli._multiplesFive(3)
    with pytest.raises(TypeError):
        cli._multiplesFive("")
        cli._multiplesFive(None)

def test_multiplesFiveAndThree():
    assert True == cli._multiplesThreeAndFive(15)
    assert False == cli._multiplesThreeAndFive(3)
    assert False == cli._multiplesThreeAndFive(5)
    assert False == cli._multiplesThreeAndFive(7)
    with pytest.raises(TypeError):
        cli._multiplesThreeAndFive("")
        cli._multiplesThreeAndFive(None)

def test_printMultiples():
     assert None == cli._printMultiples(0, 100)
     assert None == cli._printMultiples(-5, 20)
     assert None == cli._printMultiples(20, 20)
    
