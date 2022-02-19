from pages.base_page import BasePage
from pages.cart_page import CartPage
from pages.product_page_locators import ProductPageLocators
from constants import COUNT


class ProductPage(BasePage):
    def get_cost(self):
        one_cost = self.find_element(ProductPageLocators.ONE_COST).text
        one_cost = int(one_cost[1:])
        return one_cost

    def add_to_cart(self):
        add_count = self.find_element(ProductPageLocators.ADD_TO_COUNT_LOCATOR)
        add_count.clear()
        add_count.send_keys(COUNT)
        add_to_cart = self.find_element(ProductPageLocators.ADD_TO_CART_BUTTON_LOCATOR)
        add_to_cart.click()

    def open_cart(self):
        open_cart = self.find_element(ProductPageLocators.OPEN_CART)
        open_cart.click()
        return CartPage(self.driver, self.driver.current_url)

