from playwright.sync_api import sync_playwright


def before_all(context):
    context.playwright_instance = sync_playwright().start()  # Start Playwright instance

    # Launch Playwright browser instance
    browser = context.playwright_instance.chromium.launch(headless=False, slow_mo=1000, channel="chrome")
    context.page = browser.new_page()
    context.page.set_viewport_size({"width": 1800, "height": 1080})


def after_all(context):
    # Closing Playwright browser instance
    context.playwright_instance.stop()
