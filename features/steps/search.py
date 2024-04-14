from behave import *
from selenium.common.exceptions import NoSuchElementException


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
    context.page.wait_for_timeout(3000)
    try:
        header = context.page.locator('.oxd-userdropdown')
        if header.is_visible():
            header.click()
            logout = context.page.locator( "div.oxd-topbar-header li:nth-child(4) a")
            logout.click()
    except NoSuchElementException:
        # Handle the case where the header is not found (e.g., log a message)
        print("Header not found. Skipping logout.")