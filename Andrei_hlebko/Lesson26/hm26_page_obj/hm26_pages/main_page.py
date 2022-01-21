from Lesson26.hm26_page_obj.hm26_pages.base_page import BasePage
from Lesson26.hm26_page_obj.hm26_pages.basket_page import BasketPage
from Lesson26.hm26_page_obj.hm26_pages.books_page import BooksPage
from Lesson26.hm26_page_obj.hm26_pages.books_page_locators import BookPageLocators
from Lesson26.hm26_page_obj.hm26_pages.fiction_page import FictionPage
from Lesson26.hm26_page_obj.hm26_pages.login_page import LoginPage
from Lesson26.hm26_page_obj.hm26_pages.main_page_locators import MainPageLocators


class MainPage(BasePage):
    URL = "http://selenium1py.pythonanywhere.com/en-gb/"

    def __init__(self, driver):
        super().__init__(driver, self.URL)

    def open_login_page(self):
        """
        The func open login page
        """
        login_link = self.find_element(MainPageLocators.LOGIN_LINK_LOCATORS)
        login_link.click()
        return LoginPage(self.driver, self.driver.current_url)

    def open_books_page(self):
        """
        The func open books page
        """
        book_link = self.find_element(MainPageLocators.BOOK_LINK_LOCATORS)
        book_link.click()
        return BooksPage(self.driver, self.driver.current_url)

    def add_one_book_in_basket(self):
        first_book_btn = self.find_element(MainPageLocators.ADD_FIRST_BOOK_TO_BASKET)
        first_book_btn.click()
        return BasketPage(self.driver, self.driver.current_url)

    def add_one_book_in_basket_and_switch_to_basket(self):
        first_book_btn = self.find_element(MainPageLocators.ADD_FIRST_BOOK_TO_BASKET)
        first_book_btn.click()
        view_basket_btn = self.find_element(MainPageLocators.VIEW_BASKET_BUTTON_LOCATOR)
        view_basket_btn.click()
        return BasketPage(self.driver, self.driver.current_url)

    def open_basket_page(self):
        """
        The func open basket page
        """
        basket_link = self.find_element(MainPageLocators.VIEW_BASKET_BUTTON_LOCATOR)
        basket_link.click()
        return BasketPage(self.driver, self.driver.current_url)

    def open_books_fiction_page(self):
        """
        Open books link after open fiction link, and we are checking on the right page or not
        """
        all_products_link = self.find_element(MainPageLocators.ALL_PRODUCTS_LINK_LOCATORS)
        all_products_link.click()
        fiction_link = self.find_element(BookPageLocators.FICTION_LINK_LOCATOR)
        fiction_link.click()
        return FictionPage(self.driver, self.driver.current_url)
