from behave import fixture, use_fixture
from playwright.async_api import async_playwright
from behave.api.async_step import async_run_until_complete


@fixture
async def browser_chrome(context):
    p = await async_playwright().start()
    browser = await p.chromium.launch(headless=False, slow_mo=500, channel="chrome")  # Launching Chromium browser
    context.page = await browser.new_page()
    return context.page


@async_run_until_complete
async def before_scenario(context, scenario):
    await use_fixture(browser_chrome, context)
