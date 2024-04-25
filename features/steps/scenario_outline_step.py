from behave import *
from selenium.common.exceptions import NoSuchElementException


@when('User is Already Logged In Performed Logout')
def step_impt(context):
    try:
        header = context.page.locator('.oxd-userdropdown')
        if header.is_visible():
            header.click()
            logout = context.page.locator("div.oxd-topbar-header li:nth-child(4) a")
            logout.click()
    except NoSuchElementException:
        # Handle the case where the header is not found (e.g., log a message)
        print("Header not found. Skipping logout.")


@given("the user is on the login page")
def step_impl(context):
    context.page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")


@when('the user enters "{username}" and "{password}"')
def step_impl(context, username, password):
    context.page.fill('input[name="username"]', username)
    context.page.fill('input[name="password"]', password)


@then('the user should be logged in successfully')
def step_impl(context):
    loginbtn = context.page.locator(".orangehrm-login-button")
    loginbtn.click()
    context.page.wait_for_timeout(3000)
    try:
        header = context.page.locator('.oxd-userdropdown')
        if header.is_visible():
            header.click()
            logout = context.page.locator("div.oxd-topbar-header li:nth-child(4) a")
            logout.click()
    except NoSuchElementException:
        # Handle the case where the header is not found (e.g., log a message)
        print("Header not found. Skipping logout.")
