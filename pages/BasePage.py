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
        element = None
        if locator_type.endswith("id"):
            element = self.page.query_selector(f'#{locator_value}')
        elif locator_type.endswith("name"):
            element = self.page.query_selector(f'[name="{locator_value}"]')
        elif locator_type.endswith("class_name"):
            element = self.page.query_selector(f'.{locator_value}')
        elif locator_type.endswith("link_text"):
            element = self.page.query_selector(f'text="{locator_value}"')
        elif locator_type.endswith("xpath"):
            element = self.page.query_selector(f'xpath={locator_value}')
        elif locator_type.endswith("css"):
            element = self.page.query_selector(locator_value)
        return element

    def retrieved_element_text_contains(self, locator_type, locator_value, expected_text):
        element = self.get_element(locator_type, locator_value)
        return expected_text in element.text()

    def retrieved_element_text_equals(self, locator_type, locator_value, expected_text):
        element = self.get_element(locator_type, locator_value)
        return element.text() == expected_text

    def display_status(self, locator_type, locator_value):
        element = self.get_element(locator_type, locator_value)
        return element.is_visible()
