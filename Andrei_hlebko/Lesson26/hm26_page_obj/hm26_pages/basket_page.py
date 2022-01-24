from Lesson26.hm26_page_obj.hm26_pages.base_page import BasePage
from Lesson26.hm26_page_obj.hm26_pages.basket_page_locators import BasketPageLocators
from Lesson26.hm26_page_obj.hm26_pages.main_page_locators import MainPageLocators


class BasketPage(BasePage):
    def get_basket_page_header(self):
        """

        The func check header basket text
        """
        return self.find_element(BasketPageLocators.HEADER_BASKET)

    def check_basket_empty(self):
        """

        The func check is basket empty or not
        """
        return self.find_element(BasketPageLocators.BASKET_IS_EMPTY)

    def check_proceed_to_checkout_btn(self):
        return self.find_element(BasketPageLocators.PROCEED_TO_CHECKOUT_BTN)

    def get_inf_book_was_added(self):
        return self.find_element(MainPageLocators.BOOK_WAS_ADDED)
