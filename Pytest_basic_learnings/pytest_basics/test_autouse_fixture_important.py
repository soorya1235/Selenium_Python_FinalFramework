import pytest
from datetime import datetime, time

"""
Here we can use autouse fixture inside the testcase,or inside the conftest.py file
if it is defined there,it will automatically run for all the testcases.
There is no need to mention as part of the class so i am commenting here.
"""

# @pytest.fixture(autouse=True)
# def time_calculator():
#     print(f" Test started: {datetime.now().strftime('%d-%m-%Y %H:%M')} ")
#     yield
#     print(f" Test ended: {datetime.now().strftime('%d-%m-%Y %H:%M')} ")

#@pytest.mark.usefixtures("time_calculator")
class Test_Auto_Fixture:

    def test_testcase_1(self):
        print("Testcase 1")

    def test_testcase_2(self):
        print("Testcase 2")

"""
Auto use fixture will be run for all the testcase to calcualte the exeuction time
"""