
# This file is used by behave to do some background setup including an obj we'll need
# Context Object, also a place to add any setup and teardown functions for our tests.
# These functions must use behave naming conventions
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

from features.pages.mechs_home_page import MechsHomePage
from features.pages.mechs_page import MechsPage


def before_all(context):
    # todo Replace the chromedriver PATH with your PATH inside quotes below
    driver: WebDriver = webdriver.Chrome('/Users/David/Revature/chromedriver')
    mechs_page = MechsPage(driver)

    # can I add this line and include another Page??
    mechs_home = MechsHomePage(driver)

    context.driver = driver
    context.mechs_page = mechs_page
    context.mechs_home = mechs_home
    print("started webdriver")


def after_all(context):
    context.driver.quit()

    print("Ended webdriver")
