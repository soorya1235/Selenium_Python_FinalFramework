def test():
    print("hello")

""""
pytest test_pytest_parallel_exeuction_xdist.py -n 3,we an alos configure this in pytest.ini file
Note if we put "addopts = -n3" under after pytest,it will default exeucte 3 times..for all the test
example

[pytest]
addopts = -n3
markers =
         functional
         regression
        
"""