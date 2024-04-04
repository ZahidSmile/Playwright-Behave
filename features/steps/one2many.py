from behave import *
from behave.api.async_step import async_run_until_complete
from selenium.common.exceptions import NoSuchElementException


@given("the user is on the login page")
# @async_run_until_complete
async def step_impl(context):
    await context.page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")


@when('the user enters "{username}" and "{password}"')
# @async_run_until_complete
async def step_impl(context, username, password):
    await context.page.fill('input[name="username"]', username)
    await context.page.fill('input[name="password"]', password)


@then('the user should be logged in successfully')
# @async_run_until_complete
async def step_impl(context):
    loginbtn = context.page.locator(".orangehrm-login-button")
    await loginbtn.click()
    try:
        header = context.page.locator('.oxd-userdropdown')
        if await header.is_visible():
            await header.click()
            logout = context.page.locator( "div.oxd-topbar-header li:nth-child(4) a")
            await logout.click()
    except NoSuchElementException:
        # Handle the case where the header is not found (e.g., log a message)
        print("Header not found. Skipping logout.")

