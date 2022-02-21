from eugene_shurpach.diploma.tools.base_page import BasePage
from eugene_shurpach.diploma.tools.success_page_locators import SuccessPageLocators


class SuccessPage(BasePage):

    def check_success_order(self):
        el = self.find_element(SuccessPageLocators.TITLE)
        return "Your order is successfully completed!" == el.text
