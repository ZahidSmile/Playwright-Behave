from behave import *


@given('I am on search field')
def step_impl(context):
    context.page.wait_for_timeout(3000)
    context.page.wait_for_selector('.oxd-input')


@when("I search admin")
def step_impl(context):
    context.page.fill('.oxd-input', 'admin')


@step("I clicked on admin")
def step_impl(context):
    context.page.get_by_role("link", name="Admin").click()


@then("I successfully landed on admin panel")
def step_impl(context):
    assert context.page.locator('.oxd-userdropdown'), 'Dropdown is not Visible'
