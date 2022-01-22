from pages.base_page import BasePage

'''Файл с описанием страницы fiction'''

class FictionPage(BasePage):
    URL = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/category/books/fiction_3/'
    TITLE = 'Fiction | Oscar - Sandbox'

    def __init__(self, driver):
        super().__init__(driver, self.URL)
