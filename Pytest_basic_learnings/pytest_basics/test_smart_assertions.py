from  smart_assertions import soft_assert, verify_expectations

def test_something():
    soft_assert(2 == 2)
    soft_assert(2 > 3, 'Message if test failed')
    soft_assert('one' != 'two', 'Some message')
    verify_expectations()
