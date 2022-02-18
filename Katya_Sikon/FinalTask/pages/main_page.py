from common import driver
from constants import EMAIL, PASSWORD
from pages.base_page import BasePage
from pages.main_page_locators import MainPageLocators
from pages.poduct_page import ProductPage


class MainPage(BasePage):
    url = "http://localhost/litecart"

    def __init__(self, driver):
        super().__init__(driver, self.url)

    def login(self):
        email = self.find_element(MainPageLocators.EMAIL_LOCATOR)
        email.send_keys(EMAIL)
        password = self.find_element(MainPageLocators.PASSWORD_LOCATOR)
        password.send_keys(PASSWORD)
        button = self.find_element(MainPageLocators.LOGIN_BUTTON_LOCATOR)
        button.click()

    def choose_green_duck(self):
        green_duck = self.find_element(MainPageLocators.GREEN_QUACK_LOCATOR)
        green_duck.click()
        return ProductPage(self.driver, self.driver.current_url)

"""
    def open_login_page(self):
        login_link = self.find_element(MainPageLocators.LOGIN_LINK_LOCATORS)
        login_link.clic()
        return LoginPage(self.driver, self.driver.current_url)

    def get_oscar_reference(self):
        reference = self.find_element(MainPageLocators.OSCAR_REF_LOCATORS)
        return reference

    def open_books_page(self):
        books_link = self.find_element(MainPageLocators.BOOKS_REF_LOCATORS)
        books_link.click()
        return BooksPage(self.driver, self.driver.current_url)
"""