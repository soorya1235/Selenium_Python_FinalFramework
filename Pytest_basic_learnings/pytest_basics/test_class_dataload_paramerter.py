import pytest
"""
Note class name should be in "Capital T" like Test_demo,else if we give test_demo it will fail
"""


@pytest.mark.usefixtures("dataload")
class Test_demo:

    def test_loading_example(self,dataload):
        print(dataload)

    def test_parameter_example(self,data_parameter):
        print(data_parameter)

    @pytest.fixture()
    def load_multiple_data(self):
        return ['a','b','c']

    @pytest.mark.usefixtures("load_multiple_data")
    def test_local_fixture(self,load_multiple_data):
        print(load_multiple_data)