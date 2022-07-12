import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

#
# from selenium.webdriver.chrome import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager


def getdata():
    return [
        ("user1","passowrd1"),
        ("user2", "passowrd2"),
        ("user3", "passowrd3")

    ]

def setup_function():
    global driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("http://facebook.com")
    driver.maximize_window()


def teardown_function():
    driver.quit()




@pytest.mark.parametrize("username,password",getdata())
def test_login(username,password):
    driver.find_element(By.ID,"email").send_keys(username)
    driver.find_element(By.ID,"pass").send_keys(password)

"""
To exeuct in parallel use pytest test_pytest_paralle.py -n 3,this will exeucte 3 times the launching of browser
"""