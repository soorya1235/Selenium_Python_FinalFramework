import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import logging
import inspect
import os


@pytest.mark.usefixtures("setup")
class BaseClass:

  def getLogger(self):
    loggerName = inspect.stack()[1][3]
    logger = logging.getLogger(loggerName)
    print(os.getcwd())
    filename = r"C:\Final_Framework\Sel_Framework\Log\logfile.log"
    fileHandler = logging.FileHandler(filename)
    formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
    fileHandler.setFormatter(formatter)

    logger.addHandler(fileHandler)  # filehandler object

    logger.setLevel(logging.DEBUG)
    return logger

  def verifyLinkPresence(self, text):
    element = WebDriverWait(self.driver, 20).until(
      EC.presence_of_element_located((By.XPATH, text)))
    element.click()



