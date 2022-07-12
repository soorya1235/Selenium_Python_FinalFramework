import pytest

@pytest.mark.functional
def test_login():
    print("Exeucting login test")

@pytest.mark.regression
def test_user_reg():
    print("User registration")

@pytest.mark.functional
def test_compose_email():
    print("Composing email")

@pytest.mark.skip
def test_skiptest():
    print("skip test")

"""
to execute use py.test test_pytest_markers_registration.py -m regression
to execute use py.test test_pytest_markers_registration.py -m "not regression"  [will run the functional testcases]
"""