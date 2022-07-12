import pytest_check as check

def test_one():
    check.equal("1abcd","abcd","Both are not equal")
    check.greater(112,10,"Not greater than")

    check.equal("abcd", "adsfds", "Both are not equal")
    check.greater(2, 10, "Not greater cthan")