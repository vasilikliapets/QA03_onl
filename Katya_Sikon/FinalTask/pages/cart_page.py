from pages.base_page import BasePage
from pages.cart_page_locators import CartPageLocators


class CartPage(BasePage):

    def get_total_cost(self):
        total_cost = self.find_element(CartPageLocators.TOTAL_COST_LOCATOR).text
        total_cost = float(total_cost[1:])
        return total_cost

    def confirm_order(self):
        confirm_order = self.find_element(CartPageLocators.CONFIRM_ORDER_LOCATOR)
        confirm_order.click()

    def duck_in_cart(self):
        box_cart = self.find_element(CartPageLocators.BOX_CART_LOCATOR)
        return box_cart