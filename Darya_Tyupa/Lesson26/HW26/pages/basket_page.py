from HW26.pages.base_page import BasePage
from HW26.pages.basket_page_locators import BasketPageLocators


class BasketPage(BasePage):

    def get_basket_page_title(self):
        return self.find_element(BasketPageLocators.BASKET_TITLE_LOCATOR)

    def get_empty_text(self):
        return self.find_element(BasketPageLocators.EMPTY_TEXT_LOCATOR)

    def get_order_area(self):
        return self.find_element(BasketPageLocators.ORDER_AREA_LOCATOR)
