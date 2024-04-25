from pages.basepage import BasePage


class OrangehrmUpload(BasePage):
    def __init__(self, page):
        super().__init__(page)

    def profile_page(self):
        self.page.wait_for_load_state()
        self.page.get_by_role("link", name="My Info").click()

    def click_on_image(self):
        self.page.wait_for_selector('.orangehrm-edit-employee .employee-image')
        self.page.locator('.orangehrm-edit-employee .employee-image').click()

    def verify_upload_page(self):
        self.page.wait_for_selector('.orangehrm-main-title')
        element = self.page.locator('.orangehrm-main-title')
        assert element.text_content() == 'Change Profile Picture'

    def get_file(self):
        self.page.wait_for_load_state()
        self.upload_image('.oxd-file-input', 'pages/images.jpeg')

    def upload_file(self):
        self.page.locator('.oxd-button').click()

    def verify_upload(self):
        success_message = self.page.wait_for_selector('.oxd-toast-content--success')
        success_text = success_message.text_content()
        print("Success Message:", success_text)
