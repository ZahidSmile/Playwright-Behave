from behave import given, when, then


@given('I am on the login page')
def step_impl(context):
    context.page.goto('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')


@when('I enter valid credentials')
def step_impl(context):
    context.page.fill('input[name="username"]', 'Admin')
    context.page.fill('input[name="password"]', 'admin123')


@when('I click the login button')
def step_impl(context):
    loginbtn = context.page.locator('.orangehrm-login-button')
    loginbtn.click()


@then('I should be redirected to the dashboard')
def step_impl(context):
    assert context.page.url == 'https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index'
