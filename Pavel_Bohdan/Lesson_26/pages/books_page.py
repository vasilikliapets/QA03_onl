from pages.base_page import BasePage
from pages.books_page_locators import BooksPageLocators
from pages.main_page_locators import MainPageLocators
from pages.search_page_locators import SearchPageLocators

'''Файл с описанием страницы Books'''

class BooksPage(BasePage):
    URL = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/category/books_2/'
    TITLE = 'Books | Oscar - Sandbox'

    def __init__(self, driver):
        super().__init__(driver, self.URL)

    def get_title(self):
        '''Функция возвращает название страницы'''
        return self.driver.title

    def find_book_by_name(self, book_name):
        '''Функция возвращает страницу с найденной книгой'''
        search_field = self.find_element(
            MainPageLocators.SEARCH_FIELD_LOCATORS)
        search_field.send_keys(book_name)
        search_field.submit()
        book = self.find_element(SearchPageLocators.BOOKS_LOCATOR)
        book.click()
        return BooksPage(self.driver)

