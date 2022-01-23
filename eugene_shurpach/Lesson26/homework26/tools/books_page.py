from eugene_shurpach.Lesson26.homework26.tools.base_page import BasePage
from eugene_shurpach.Lesson26.homework26.tools.books_page_locators import BooksPageLocators


class BooksPage(BasePage):

    def get_header(self):
        element = self.find_element(BooksPageLocators.HEADER_LOCATORS)
        return element

    def get_site_tree(self):
        element = self.find_element(BooksPageLocators.SITE_TREE_LOCATORS)
        return element
