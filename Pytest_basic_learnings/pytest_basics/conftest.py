from datetime import datetime

import pytest

@pytest.fixture(autouse=True)
def time_calculator():
    print(f" Test started: {datetime.now().strftime('%d-%m-%Y %H:%M')} ")
    yield
    print(f" Test ended: {datetime.now().strftime('%d-%m-%Y %H:%M')} ")


@pytest.fixture(scope="class")
def setup():
    print("I will be executing first")
    yield
    print("I will be executing last")

@pytest.fixture()
def dataload():
    return ["soorya","saravanan"]

@pytest.fixture(params=[("chrome","soorya","saravanan"),"firefox","IE"])
def data_parameter(request):
    return request.param