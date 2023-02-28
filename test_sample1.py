import pytest

a = ["Bob", "Bill", "Pete"]
c ={}
for i in a:
    sum = 0
    for x in i:
        sum+=ord(x)
    c[i] = sum
print(f"{c}")

def test_bob_length():
    assert c["Bob"] == 275
def test_bill_length():
    assert c["Bill"] != 388