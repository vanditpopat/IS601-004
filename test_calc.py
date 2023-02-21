import pytest
from calc import calc

def test_Add():
    c =calc()
    c.add(2,7)
    assert c.ans == 9