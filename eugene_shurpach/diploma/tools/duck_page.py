from selenium.webdriver import Keys
from eugene_shurpach.diploma.tools.base_page import BasePage
from eugene_shurpach.diploma.tools.constants import COUNT
from eugene_shurpach.diploma.tools.duck_page_locators import DuckPageLocators


class DuckPage(BasePage):
    def add_duck(self):
        add_quantity = self.find_element(DuckPageLocators.INPUT_QUANTITY)
        add_quantity.send_keys(Keys.DELETE)
        add_quantity.send_keys(COUNT)
        add_duck_in_basket = self.find_element(DuckPageLocators.BUTTON_ADD)
        add_duck_in_basket.click()

    def get_price(self):
        price_for_duck = self.find_element(DuckPageLocators.PRICE).text
        price_int = int(price_for_duck[1:])
        return price_int
