

class GooglePage:
    def __init__(self, page):
        self.page = page

    def open_page(self):
        self.page.goto('https://www.google.com/')

    def search_on_page(self, keyword):
        self.page.fill('#APjFqb', keyword)
        self.page.press('#APjFqb', 'Enter')

    def verify_search(self):
        assert self.page.title() == 'Playwright - Google Search'
