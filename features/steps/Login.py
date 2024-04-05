from behave import given, when, then
from behave.api.async_step import async_run_until_complete


@given('I am on the login page')
@async_run_until_complete
async def step_impl(context):
    await context.page.goto('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')


@when('I enter valid credentials')
@async_run_until_complete
async def step_impl(context):
    await context.page.fill('input[name="username"]', 'Admin')
    await context.page.fill('input[name="password"]', 'admin123')


@when('I click the login button')
@async_run_until_complete
async def step_impl(context):
    loginbtn = context.page.locator('.orangehrm-login-button')
    await loginbtn.click()


@then('I should be redirected to the dashboard')
@async_run_until_complete
async def step_impl(context):
    assert context.page.url == 'https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index'
