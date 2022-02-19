from constants import EMAIL, PASSWORD
from pages.base_page import BasePage
from pages.main_page_locators import MainPageLocators
from pages.product_page import ProductPage


class MainPage(BasePage):
    url = "http://localhost/litecart"

    def __init__(self, driver):
        super().__init__(driver, self.url)

    def login(self):
        self.open()
        email = self.find_element(MainPageLocators.EMAIL_LOCATOR)
        email.send_keys(EMAIL)
        password = self.find_element(MainPageLocators.PASSWORD_LOCATOR)
        password.send_keys(PASSWORD)
        button = self.find_element(MainPageLocators.LOGIN_BUTTON_LOCATOR)
        button.click()

    def choose_green_duck(self):
        green_duck = self.find_element(MainPageLocators.GREEN_DUCK_LOCATOR)
        green_duck.click()
        return ProductPage(self.driver, self.driver.current_url)
