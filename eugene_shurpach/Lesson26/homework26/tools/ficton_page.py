from eugene_shurpach.Lesson26.homework26.tools.base_page import BasePage
from eugene_shurpach.Lesson26.homework26.tools.fiction_page_locators import FictionPageLocators


class FictionPage(BasePage):

    def get_header(self):
        element = self.find_element(FictionPageLocators.HEADER_LOCATORS)
        return element
    