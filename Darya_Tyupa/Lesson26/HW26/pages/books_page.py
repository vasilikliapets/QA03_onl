import time

from HW26.pages.base_page import BasePage
from HW26.pages.books_page_locators import BooksPageLocators
from HW26.pages.fiction_page import FictionPage
from HW26.pages.search_page import SearchPage


class BooksPage(BasePage):

    def get_books_page_title(self):
        return self.find_element(BooksPageLocators.BOOKS_TITLE_LOCATOR)

    def get_fiction_link(self):
        return self.find_element(BooksPageLocators.FICTION_LINK_LOCATOR)

    def get_site_tree(self):
        return self.find_element(BooksPageLocators.SITE_TREE_LOCATORS)


    def open_search_book(self, book_name):
        search_field = self.find_element(BooksPageLocators.SEARCH_FIELD_LOCATOR)
        search_field.send_keys(book_name)
        search_button = self.find_element(BooksPageLocators.SEARCH_BUTTON_LOCATOR)
        search_button.click()
        return SearchPage(self.driver, self.driver.current_url)

    def open_fiction_page(self):
        fiction_link = self.find_element(BooksPageLocators.FICTION_LINK_LOCATOR)
        time.sleep(3)
        fiction_link.click()
        return FictionPage(self.driver, self.driver.current_url)

