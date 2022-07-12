import pytest_check as check


def test_one():
    check.equal("abcd","bbbb")

def test_two():
    check.greater(10,9)

def test_three():
    check.not_equal(2,4)

#Refer :https://blog.testproject.io/2020/08/11/non-blocking-assertion-failures-with-pytest-check/