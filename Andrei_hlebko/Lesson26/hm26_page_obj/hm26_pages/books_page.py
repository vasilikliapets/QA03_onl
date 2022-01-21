from Lesson26.hm26_page_obj.hm26_pages.base_page import BasePage
from Lesson26.hm26_page_obj.hm26_pages.books_page_locators import BookPageLocators
from Lesson26.hm26_page_obj.hm26_pages.search_page import SearchPage


class BooksPage(BasePage):
    def get_books_header(self):
        """

        The func get header books text
        """
        return self.find_element(BookPageLocators.TITLE_BOOK_LOCATOR)

    def get_site_tree(self):
        return self.find_element(BookPageLocators.SITE_TREE_LOCATORS)

    def search_book(self, book_name):
        """
        The func get book name, and find book
        """
        input_search = self.find_element(BookPageLocators.INPUT_SEARCH_LOCATORS)
        input_search.send_keys(book_name)
        input_search.click()
        button = self.find_element(BookPageLocators.BUTTON_SEARCH_LOCATORS)
        button.click()
        # input_search.submit()

    def open_search_book(self, book_name):
        """
        The func get book name, find and open book which we search
        """
        input_search = self.find_element(BookPageLocators.INPUT_SEARCH_LOCATORS)  # INPUT_SEARCH_LOCATORS
        input_search.send_keys(book_name)
        button = self.find_element(BookPageLocators.BUTTON_SEARCH_LOCATORS)
        button.click()
        return SearchPage(self.driver, self.driver.current_url)
