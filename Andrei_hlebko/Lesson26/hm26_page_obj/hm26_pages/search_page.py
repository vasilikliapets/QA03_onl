from Lesson26.hm26_page_obj.hm26_pages.base_page import BasePage
from Lesson26.hm26_page_obj.hm26_pages.search_book_locators import SearchPageLocators


class SearchPage(BasePage):
    def open_image_book(self):
        image_book = self.find_element(SearchPageLocators.BOOK_IMAGE_LOCATORS)
        image_book.click()
        return self.driver.current_url

    def get_title(self):
        return self.driver.title
