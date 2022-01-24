from Lesson26.hm26_page_obj.hm26_pages.base_page import BasePage
from Lesson26.hm26_page_obj.hm26_pages.fiction_page_locators import FictionPageLocators


class FictionPage(BasePage):
    def get_fiction_page_header(self):
        """
        The func get and return Header Fiction text
        """
        return self.find_element(FictionPageLocators.HEADER_FICTION)
