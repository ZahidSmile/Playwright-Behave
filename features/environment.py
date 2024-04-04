from playwright.sync_api import sync_playwright


def before_feature(context, feature):
    context.browser = sync_playwright().start().chromium.launch(headless=False, slow_mo=500, channel="chrome")
    context.page = context.browser.new_page()


def after_feature(context, feature):
    context.page.close()
    context.browser.close()