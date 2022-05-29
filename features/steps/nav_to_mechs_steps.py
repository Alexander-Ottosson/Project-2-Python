import unittest

from behave import given, when, then
from selenium.webdriver.chrome.webdriver import WebDriver

from features.pages.mechs_home_page import MechsHomePage

unittest = unittest.TestCase()


@given('The User is on the Mechs Home Page')
def on_index_page(context):
    driver: WebDriver = context.driver
    # todo Replace what's inside quotes with your "index.html" file PATH
    driver.get('file:///Users/David/Revature/Projects/P2/Project-2-Front-End/index.html')


@when('The User clicks on Mechs')
def press_mechs_btn(context):
    mechs_home: MechsHomePage = context.mechs_home
    mechs_home.mechs_link().click()


@then('The User can view Mechs Page')
def verify_title_page(context):
    driver: WebDriver = context.driver
    # assert driver.title == "Mechs"
    unittest.assertEquals(driver.title, "Mechs")


@when(u'The User clicks on Login')
def step_impl(context):
    mechs_home: MechsHomePage = context.mechs_home
    mechs_home.login_link().click()


@then(u'The User can view Login Page')
def step_impl(context):
    driver: WebDriver = context.driver
    unittest.assertEquals(driver.title, "Login")