from eugene_shurpach.Lesson26.homework26.tools.base_page import BasePage
from eugene_shurpach.Lesson26.homework26.tools.basket_page import BasketPage
from eugene_shurpach.Lesson26.homework26.tools.books_page import BooksPage
from eugene_shurpach.Lesson26.homework26.tools.books_page_locators import BooksPageLocators
from eugene_shurpach.Lesson26.homework26.tools.ficton_page import FictionPage
from eugene_shurpach.Lesson26.homework26.tools.login_page import LoginPage
from eugene_shurpach.Lesson26.homework26.tools.main_page_locators import MainPageLocators


class MainPage(BasePage):
    URL = "http://selenium1py.pythonanywhere.com/en-gb/"

    def __init__(self, driver):
        super().__init__(driver, self.URL)

    def open_login_page(self):
        login_link = self.find_element(MainPageLocators.LOGIN_LINK_LOCATORS)
        login_link.click()
        return LoginPage(self.driver, self.driver.current_url)

    def get_oscar_reference(self):
        reference = self.find_element(MainPageLocators.OSCAR_REF_LOCATORS)
        return reference

    def open_books_page(self):
        books_link = self.find_element(MainPageLocators.BOOKS_REF_LOCATORS)
        books_link.click()
        return BooksPage(self.driver, self.driver.current_url)

    def open_fiction_page(self):
        books_link = self.find_element(MainPageLocators.BOOKS_REF_LOCATORS)
        books_link.click()
        fiction_page = self.find_element(BooksPageLocators.FICTION_LOCATORS)
        fiction_page.click()
        return FictionPage(self.driver, self.driver.current_url)

    def open_basket_page(self):
        basket_link = self.find_element(MainPageLocators.BASKET_LOCATORS)
        basket_link.click()
        return BasketPage(self.driver, self.driver.current_url)