import unittest
from behave import given, when, then
from selenium.webdriver.chrome.webdriver import WebDriver

from features.pages.mechs_page import MechsPage

unittest = unittest.TestCase()


@given('The User is on the Mechs Page')
def get_available_mechs(context):
    driver: WebDriver = context.driver
    # todo Replace what's inside quotes with your "mechs.html" file PATH
    driver.get('file:///Users/David/Revature/Projects/P2/Project-2-Front-End/mechs.html')


@when('The User clicks on Available')
def filter_available_mechs(context):
    # MechsPage = context.mechs_page comes from environment.py
    filter_avail: MechsPage = context.mechs_page
    filter_avail.filter_available().click()


@then('The User can view Available Mechs')
def verify_view_available(context):
    driver: WebDriver = context.driver
    # assert driver.title == "Mechs"
    unittest.assertEquals(driver.title, "Mechs")