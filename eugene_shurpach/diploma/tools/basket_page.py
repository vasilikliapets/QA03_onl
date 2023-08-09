from eugene_shurpach.diploma.tools.base_page import BasePage
from eugene_shurpach.diploma.tools.basket_page_locators import BasketPageLocators
from eugene_shurpach.diploma.tools.success_page import SuccessPage


class BasketPage(BasePage):

    def confirm_order(self):
        el = self.find_element(BasketPageLocators.CONFIRM_BUTTON)
        el.click()
        return SuccessPage(self.driver, self.driver.current_url)

    def get_unit_cost(self):
        el = self.find_element(BasketPageLocators.UNIT_COST).text
        unit_cost = float(el[1:])
        return unit_cost

    def get_total_cost(self):
        el = self.find_element(BasketPageLocators.TOTAL).text
        total_cost = float(el[1:])
        return total_cost
