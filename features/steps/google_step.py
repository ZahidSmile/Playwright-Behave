from behave import *
from pages.google_page import GooglePage


@given('I am on search page')
def opening_browser(context):
    context.browser = GooglePage(context.page)
    context.browser.open_page()


@when('I searched Playwright')
def searching_on_page(context):
    context.browser.search_on_page()


@then('Search should be displayed')
def verify_the_title(context):
    context.browser.verify_search()