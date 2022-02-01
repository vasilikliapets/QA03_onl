
from HW26.pages.base_page import BasePage
from HW26.pages.fiction_page_locators import FictionPageLocators


class FictionPage(BasePage):

    def get_fiction_page_title(self):
        return self.find_element(FictionPageLocators.FICTION_PAGE_TITLE).text

