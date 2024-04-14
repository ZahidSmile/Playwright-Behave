from playwright.sync_api import sync_playwright


def before_feature(context, feature):
    context.browsers = {}  # Dictionary to store browser instances
    context.playwright_instance = sync_playwright().start()  # Start Playwright instance
    browser_type = "chromium"  # Change this according to your requirement

    # Launch Playwright browser instance
    browser = context.playwright_instance[browser_type].launch(headless=False, slow_mo=500, channel="chrome")
    context.browsers[browser_type] = browser
    context.page = browser.new_page()


def after_feature(context, feature):
    # Close all browser instances
    for browser in context.browsers.values():
        browser.close()

    # Stop Playwright instance
    context.playwright_instance.stop()