import os
import time
from playwright.sync_api import expect
import logging

logging.basicConfig(filename='savyour_log_file.log', level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')


class BasePage:
    def __init__(self, page):
        self.page = page

    def open_url(self, add_url):
        self.page.goto(add_url)
        time.sleep(3)

    def click_on_element(self, locator_type, locator_value):
        element = self.get_element(locator_type, locator_value)
        element.first.click()

    def verify_page_title(self, expected_title):
        return self.page.title() == expected_title

    def type_into_element(self, locator_type, locator_value, text_to_entered):
        element = self.get_element(locator_type, locator_value)
        element.click()
        element.first.fill(text_to_entered)

    def get_element(self, locator_type, locator_value):
        switcher = {
            "id": f'#{locator_value}',
            "name": f'[name="{locator_value}"]',
            "class_name": f'.{locator_value}',
            "link_text": f'text="{locator_value}"',
            "xpath": f'xpath={locator_value}',
            "css": locator_value
        }
        element = self.page.locator(switcher.get(locator_type, locator_value))
        return element

    def retrieved_element_text_contains(self, locator_type, locator_value, expected_text):
        element = self.get_element(locator_type, locator_value)
        return expected_text in element.text_content()

    def retrieved_element_text_equals(self, locator_type, locator_value, expected_text):
        element = self.get_element(locator_type, locator_value)
        return element.text_content() == expected_text

    def display_status(self, locator_type, locator_value):
        element = self.get_element(locator_type, locator_value)
        time.sleep(2)
        return element.is_visible()

    def upload_image(self, locator_value, image_path):
        # Construct the absolute file path
        current_working_dir = os.getcwd()
        file_path = os.path.join(current_working_dir, image_path)

        # Upload the file to the element
        self.page.set_input_files(locator_value, file_path)
        return file_path

    def select_by_role(self, role_name, role_value):
        element = expect(self.page.get_by_role(role_name, name=role_value)).to_be_visible()
        self.page.get_by_role(role_name, name=role_value).first.click()
        return element

    def select_by_text(self, text_value):
        element = expect(self.page.get_by_text(text_value)).to_be_visible()
        self.page.get_by_text(text_value).first.click()
        return element

    #
    def select_by_placeholder(self, placeholder_value):
        element = self.page.get_by_placeholder(placeholder_value)
        return element

    def select_by_alt_text(self, alt_text):
        element = self.page.get_by_alt_text(alt_text)
        return element

    def select_all_elements(self, common_locator_value):
        element = self.page.query_selector_all(common_locator_value)
        return element

    def type_as_keyboard(self, locator_type, locator_value, value):
        element = self.get_element(locator_type, locator_value)
        element.click()
        element.page.keyboard.press(value)
        return element

    def verify_page_url(self, expected_value):
        if expected_value in self.page.url:
            pass

    def main_page(self):
        if self.page.url != 'https://savyour.com/pk-en/':
            self.open_url('https://savyour.com/pk-en/')

    @staticmethod
    def print_statement(value):
        logging.info(value)

