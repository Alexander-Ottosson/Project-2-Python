from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class MechsHomePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def mechs_link(self):
        return self.driver.find_element(by=By.XPATH, value='//*[@id="navbarSupportedContent"]/ul/li[2]/a')

    def login_link(self):
        return self.driver.find_element(by=By.CLASS_NAME, value="btn-primary")

    def username_field(self):
        return self.driver.find_element(by=By.ID, value="usernameInput")

    def password_field(self):
        return self.driver.find_element(by=By.ID, value="passwordInput")

    def login_btn(self):
        return self.driver.find_element(by=By.CLASS_NAME, value="btn-success")
