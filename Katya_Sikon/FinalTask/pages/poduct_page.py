from common import driver
from constants import EMAIL, PASSWORD, DUCK_QUANTITY
from pages.base_page import BasePage
from pages.main_page_locators import MainPageLocators
from pages.product_page_locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_cart(self):
        add_to_cart = self.find_element(ProductPageLocators.ADD_TO_CART_BUTTON_LOCATOR)
        add_to_cart.click()

    def change_quantity(self):
        change_quantity = self.find_element(ProductPageLocators.QUANTITY_LOCATOR)
        change_quantity.send_keys(DUCK_QUANTITY)

