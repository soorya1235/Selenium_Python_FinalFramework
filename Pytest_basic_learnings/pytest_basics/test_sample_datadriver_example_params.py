import pytest

@pytest.fixture(params=[(1,2),(3,4),(5,6)])
def test_data(request):
    return request.param


def test_using(test_data):
    print(test_data[0])
    print(test_data[1])

