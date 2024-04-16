from behave import given, when, then, step
from pages.Orangehrm_page import Orangehrm_page


@given('I am on the login page')
def login(context):
    context.page = Orangehrm_page(context.page)
    context.page.goto_page()


@when('I enter valid credentials')
def credentials(context):
    context.page.add_credentials()


@step('I click the login button')
def submit_form(context):
    context.page.submit_the_form()


@then('I should be redirected to the dashboard')
def verify_page(context):
    context.page.check_data()
