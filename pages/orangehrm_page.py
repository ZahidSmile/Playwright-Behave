import time
import json
from pages.basepage import BasePage

# Open the JSON file
with open('features/cred.json') as f:
    data = json.load(f)


class OrangehrmPage(BasePage):

    def __init__(self, page):
        super().__init__(page)

    def goto_page(self):
        orangehrm_url = data.get('orangehrm')
        self.open_url(orangehrm_url)

    def add_credentials(self):
        self.page.wait_for_load_state()
        username = data.get('username')
        password = data.get('password')
        self.display_status('css', '[name="username"]')
        self.type_into_element('name', 'username', username)
        self.type_into_element('name', 'password', password)

    def submit_the_form(self):
        if self.display_status('class_name', 'orangehrm-login-button'):
            self.click_on_element('css', '.orangehrm-login-button')

    def check_data(self):
        time.sleep(2)
        assert self.verify_page_title('OrangeHRM')


