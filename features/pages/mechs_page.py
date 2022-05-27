from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class MechsPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def filter_available(self):
        return self.driver.find_element(by=By.ID, value="onlyAvailable")
