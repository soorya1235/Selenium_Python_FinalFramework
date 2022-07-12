from selenium.webdriver.common.by import By

from Pageobjects.ShoppingEnd import ShoppingEnd


class CheckOutPage:

    def __init__(self,driver):
        self.driver = driver

    cart_items = (By.CSS_SELECTOR,'.card-title a')
    cardFooter = (By.CSS_SELECTOR, '.card-footer button')
    checkout = (By.XPATH,"//a[contains(@class,'btn')]")


    def getcartitems(self):
        return self.driver.find_elements(*CheckOutPage.cart_items)

    def checkoutcart(self):
        return self.driver.find_elements(*CheckOutPage.cardFooter)

    def gotoshopping(self):
        self.driver.find_element(*CheckOutPage.checkout).click()
        sp = ShoppingEnd(self.driver)
        return sp
