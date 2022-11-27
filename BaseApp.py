from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, xpath, time=10):
        return WebDriverWait(self.driver,time).until(EC.presence_of_element_located(xpath),
                                                      message=f"Невозможно найти элемент по xpath {xpath}")

