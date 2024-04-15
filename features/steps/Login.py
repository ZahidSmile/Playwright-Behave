from behave import given, when, then
from pages.Orangehrm_page import Orangehrm_page


@given('I am on the login page')
def step_impl(context):
    context.page = Orangehrm_page(context.page)
    context.page.goto_page()


@when('I enter valid credentials')
def step_impl(context):
    context.page.add_credentials()


@when('I click the login button')
def step_impl(context):
    context.page.submit_the_form()


@then('I should be redirected to the dashboard')
def step_impl(context):
    context.page.check_data()
