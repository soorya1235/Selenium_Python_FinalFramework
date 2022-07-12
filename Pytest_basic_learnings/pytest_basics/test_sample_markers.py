import pytest

@pytest.fixture(scope="module")
def setup():
    print("calling db connection")
    yield
    print("closing db connection")

@pytest.fixture(scope="function")
def beforefunction():
    print("Before TC called")
    yield
    print("After TC called")


# def test_one(setup,beforefunction):
#     print("HI First Test")
#
# def test_two(setup,beforefunction):
#     print("HI second Test")

@pytest.mark.usefixtures("setup","beforefunction")
def test_one(setup,beforefunction):
    print("HI First Test")

@pytest.mark.usefixtures("setup","beforefunction")
def test_two(setup,beforefunction):
    print("HI second Test")

"""
If we want to call a specif test from testcase use -k option
py.test test_sample_markers.py -k test_one or just give one
py.test test_sample_markers.py -k "not one"  [it will exeucte other tc]

"""
