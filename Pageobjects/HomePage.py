from selenium.webdriver.common.by import By

from Pageobjects.CheckOutPage import CheckOutPage


class HomePage:

    def __init__(self,driver):
        self.driver = driver

    ##define the page objects

    shop = (By.CSS_SELECTOR,"a[href*='shop']")
    name = (By.XPATH,"(//input[@name='name'])[1]")
    email = (By.XPATH,"//input[@name='email']")
    password = (By.XPATH,"//input[@id='exampleInputPassword1']")
    dropdown = (By.XPATH,"//select[@id='exampleFormControlSelect1']")
    date = (By.XPATH,"//input[@type='date']")
    submit = (By.XPATH,"//input[@type='submit']")
    message = (By.XPATH,"//div[contains(@class,'alert-success')]")

    def gotoshopitems(self):
        self.driver.find_element(*HomePage.shop).click()
        cp = CheckOutPage(self.driver)
        return cp

    def getname(self):
        return self.driver.find_element(*HomePage.name)

    def getemail(self):
        return self.driver.find_element(*HomePage.email)

    def getpass(self):
        return self.driver.find_element(*HomePage.password)

    def getdrop(self):
        return self.driver.find_element(*HomePage.dropdown)

    def getdate(self):
        return self.driver.find_element(*HomePage.date)

    def getsubmit(self):
        return self.driver.find_element(*HomePage.submit)

    def getmessage(self):
        return self.driver.find_element(*HomePage.message)
