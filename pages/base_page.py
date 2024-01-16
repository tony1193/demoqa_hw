from selenium.webdriver.common.by import By
import time
class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://www.saucedemo.com/"

    def visit(self):
        time.sleep(3)
        return self.driver.get(self.base_url)

    def find_element(self, locator):
        self.locator = locator
        return self.driver.find_element(By.CSS_SELECTOR, locator)