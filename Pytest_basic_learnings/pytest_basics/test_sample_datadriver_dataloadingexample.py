import pytest


@pytest.mark.parametrize("a,b",[(1,2),(3,4)])
def test_using(a,b):
    print(a)
    print(b)

