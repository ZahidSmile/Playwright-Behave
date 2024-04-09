from behave import *
from selenium.common.exceptions import NoSuchElementException
from behave.api.async_step import async_run_until_complete


@given('I am on search field')
@async_run_until_complete
async def step_impl(context):
    context.page.wait_for_timeout(3000)
    await context.page.wait_for_selector('.oxd-input')


@when("I search admin")
@async_run_until_complete
async def step_impl(context):
    await context.page.fill('.oxd-input', 'admin')


@step("I clicked on admin")
@async_run_until_complete
async def step_impl(context):
    await context.page.get_by_role("link", name="Admin").click()


@then("I successfully landed on admin panel")
@async_run_until_complete
async def step_impl(context):
    # context.page.locator("div").filter(has_text=re.compile(r"^AdminUser Management$")).click()
    context.page.wait_for_timeout(3000)
    try:
        header = context.page.locator('.oxd-userdropdown')
        if header.is_visible():
            await header.click()
            logout = context.page.locator( "div.oxd-topbar-header li:nth-child(4) a")
            await logout.click()
    except NoSuchElementException:
        # Handle the case where the header is not found (e.g., log a message)
        print("Header not found. Skipping logout.")

