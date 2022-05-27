import unittest

from behave import when, then
from selenium.webdriver.chrome.webdriver import WebDriver

from features.pages.mechs_home_page import MechsHomePage

unittest = unittest.TestCase()


@when('The User types {word1} in the Username Field')
def types_into_username(context, word1):
    mechs_home: MechsHomePage = context.mechs_home
    mechs_home.username_field().send_keys(word1)


@when('The User types {word2} in the Password Field')
def types_into_password(context, word2):
    mechs_home: MechsHomePage = context.mechs_home
    mechs_home.login_link().click()
    mechs_home.username_field().send_keys(word2)


@when('The User clicks the Login Button')
def presses_login_btn(context):
    mechs_home: MechsHomePage = context.mechs_home
    mechs_home.login_btn().click()


@then('The Page Title should be Login')
def verify_title_page(context):
    # test: unittest.TestCase = context.unittest
    # test.assertEquals(context.driver.title, title)
    driver: WebDriver = context.driver
    unittest.assertEquals(driver.title, "Login")
