import os
import time


class BasePage:
    def __init__(self, page):
        self.page = page

    def open_url(self, add_url):
        self.page.goto(add_url)

    def click_on_element(self, locator_type, locator_value):
        element = self.get_element(locator_type, locator_value)
        element.click()

    def verify_page_title(self, expected_title):
        return self.page.title() == expected_title

    def type_into_element(self, locator_type, locator_value, text_to_entered):
        element = self.get_element(locator_type, locator_value)
        element.click()
        element.fill(text_to_entered)

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
