from behave import *
from pages.google_page import GooglePage


@given('I am on search page')
def step_impl(context):
    context.browser = GooglePage(context.page)
    context.browser.open_page()


@when('I searched Playwright')
def step_impl(context):
    context.browser.search_on_page()


@then('Search should be displayed')
def step_impl(context):
    context.browser.verify_search()