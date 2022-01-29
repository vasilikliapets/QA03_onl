from eugene_shurpach.Lesson26.homework26.tools.base_page import BasePage
from eugene_shurpach.Lesson26.homework26.tools.basket_page_locators import BasketPageLocators


class BasketPage(BasePage):

    def get_empty_basket(self):
        element = self.find_element(BasketPageLocators.EMPTY_LOCATORS)
        return element

    def get_header(self):
        element = self.find_element(BasketPageLocators.HEADER_LOCATORS)
        return element
