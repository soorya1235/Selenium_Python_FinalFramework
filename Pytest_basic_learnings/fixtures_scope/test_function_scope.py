import pytest
from datetime import datetime

@pytest.fixture()
def only_used_once():
    print("only use fixture")

@pytest.fixture()
def light_operation():
    print("light_operation_fixutre")

@pytest.fixture()
def need_different_value_each_time():
    print(datetime.now())

@pytest.mark.usefixtures("only_used_once","light_operation","need_different_value_each_time")
def test_one_function():
     print("hello")