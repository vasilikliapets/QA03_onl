from HW26.pages.base_page import BasePage
from HW26.pages.search_page_locators import SearchPageLocators


class SearchPage(BasePage):

    def open_image_book(self):
        image_book = self.find_element(SearchPageLocators.BOOK_IMAGE_LOCATOR)
        image_book.click()
        return self.driver.current_url

    def get_title(self):
        return self.driver.title

    def get_found_book_name(self):
        return self.find_element(SearchPageLocators.FOUND_BOOK_NAME_LOCATOR)

    def get_found_book_image(self):
        return self.find_element(SearchPageLocators.FOUND_BOOK_IMAGE_LOCATOR)
