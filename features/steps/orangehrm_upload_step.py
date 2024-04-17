from pages.orangehrm_upload_page import OrangehrmUpload
from behave import given, when, step, then


@given('I am on profile page')
def verify_profile_page(context):
    context.browser = OrangehrmUpload(context.page)
    context.browser.profile_page()


@when('I click on profile picture')
def profile_picture(context):
    context.browser.click_on_image()


@then('I should landed on change profile picture page')
def verify_page(context):
    context.browser.verify_upload_page()


@when('I select the file from system')
def get_file_fromPC(context):
    context.browser.get_file()


@step('I click on save button')
def select_file(context):
    context.browser.upload_file()


@then('file should be up loaded successfully')
def verify_file_uploaded(context):
    context.browser.verify_upload()
