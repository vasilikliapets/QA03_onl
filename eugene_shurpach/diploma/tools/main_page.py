from eugene_shurpach.diploma.tools.base_page import BasePage
from eugene_shurpach.diploma.tools.basket_page import BasketPage
from eugene_shurpach.diploma.tools.constants import USER_EMAIL, USER_PASS
from eugene_shurpach.diploma.tools.ducks_page import DucksPage
from eugene_shurpach.diploma.tools.main_page_locators import MainPageLocators


class MainPage(BasePage):
    URL = "http://127.0.0.1/litecart/en/"

    def __init__(self, driver):
        super().__init__(driver, self.URL)

    def login_user(self):
        self.open()
        user_email = self.find_element(MainPageLocators.EMAIL_INPUT_LOCATORS)
        user_email.send_keys(USER_EMAIL)
        user_pass = self.find_element(MainPageLocators.PASSWORD_INPUT_LOCATORS)
        user_pass.send_keys(USER_PASS)
        submit_button = self.find_element(MainPageLocators.LOGIN_BUTTON_LOCATORS)
        submit_button.click()
        return self.driver.current_url

    def open_ducks_page(self):
        categories_link = self.find_element(MainPageLocators.CATEGORIES_LOCATORS)
        categories_link.click()
        return DucksPage(self.driver, self.driver.current_url)

    def open_basket_page(self):
        basket_link = self.find_element(MainPageLocators.BASKET_LOCATORS)
        basket_link.click()
        return BasketPage(self.driver, self.driver.current_url)
