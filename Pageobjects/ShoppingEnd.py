from selenium.webdriver.common.by import By


class ShoppingEnd:

    def __init__(self,driver):
        self.driver = driver

    exitshoppingitem = (By.XPATH,"//button[contains(text(),'Checkout')]")
    enterdataitem = (By.XPATH,"//input[@type='text']")
    chooseindia = (By.XPATH,"//a[text()='India']")
    indiachhose = "//a[text()='India']"
    checkbox = (By.XPATH,"//div[@class='checkbox checkbox-primary']")
    purchase = (By.XPATH,"//input[@value='Purchase']")
    message = (By.XPATH,"//div[contains(@class,'alert-success')]")


    def exitshopping(self):
        self.driver.find_element(*ShoppingEnd.exitshoppingitem).click()

    def enterdata(self):
        self.driver.find_element(*ShoppingEnd.enterdataitem).send_keys("india")

    def clickindia(self):
        self.driver.find_element(*ShoppingEnd.chooseindia).click()

    def clickcheckbox(self):
        self.driver.find_element(*ShoppingEnd.checkbox).click()
        self.driver.find_element(*ShoppingEnd.purchase).click()

    def getsucesstext(self):
        return self.driver.find_element(*ShoppingEnd.message)