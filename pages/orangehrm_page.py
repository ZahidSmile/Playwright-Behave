import time
from pages.basepage import BasePage


class OrangehrmPage(BasePage):

    def __init__(self, page):
        super().__init__(page)

    def goto_page(self):
        self.open_url('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')

    def add_credentials(self):
        self.type_into_element('css', 'input[name="username"]', 'Admin')
        self.type_into_element('css', 'input[name="password"]', 'admin123')

    def submit_the_form(self):
        self.click_on_element('css', '.orangehrm-login-button')

    def check_data(self):
        time.sleep(2)
        assert self.verify_page_title('OrangeHRM')


