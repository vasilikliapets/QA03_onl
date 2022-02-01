from HW26.pages.base_page import BasePage
from HW26.pages.basket_page import BasketPage
from HW26.pages.books_page import BooksPage
from HW26.pages.login_page import LoginPage
from HW26.pages.main_page_locators import MainPageLocators


class MainPage(BasePage):
    URL = "http://selenium1py.pythonanywhere.com/en-gb/"

    def __init__(self, driver):
        super().__init__(driver, self.URL)

    def open_login_page(self):
        login_link = self.find_element(MainPageLocators.LOGIN_LINK_LOCATOR)
        login_link.click()
        return LoginPage(self.driver, self.driver.current_url)

    def open_books_page(self):
        books_link = self.find_element(MainPageLocators.BOOK_LINK_LOCATOR)
        books_link.click()
        return BooksPage(self.driver, self.driver.current_url)

    def open_basket_page(self):
        basket_link = self.find_element(MainPageLocators.BASKET_LINK_LOCATOR)
        basket_link.click()
        return BasketPage(self.driver, self.driver.current_url)