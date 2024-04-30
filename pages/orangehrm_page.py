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
        self.select_by_placeholder('Username').fill(username)
        self.select_by_placeholder('Password').fill(password)

    def submit_the_form(self):
        self.select_by_role('button','Login')

    def check_data(self):
        time.sleep(2)
        assert self.verify_page_title('OrangeHRM')
