from pages.base_page import BasePage
from pages.main_page_locators import MainPageLocators
from pages.basket_page import BasketPage
from pages.fiction_page import FictionPage
from pages.books_page import BooksPage
from pages.search_page_locators import SearchPageLocators

'''Файл с описанием основной страницы'''


class MainPage(BasePage):
    URL = 'http://selenium1py.pythonanywhere.com/en-gb/'
    TITLE = 'Oscar - Sandbox'

    def __init__(self, driver):
        super().__init__(driver, self.URL)

    def open_basket_page(self):
        '''Функция  открывает и возвращает страницу корзины'''
        basket_link = self.find_element(MainPageLocators.BASKET_LINK_LOCATORS)
        basket_link.click()
        return BasketPage(self.driver)

    def open_fiction_page(self):
        '''Функция открывает и возвращает страницу fiction'''
        submenu_link = self.find_element(
            MainPageLocators.SUBMENU_LINK_LOCATORS)
        submenu_link.click()
        fiction_link = self.find_element(
            MainPageLocators.FICTION_LINK_LOCATORS)
        fiction_link.click()
        return FictionPage(self.driver)

    def open_books_page(self):
        '''Функция открывает и возвращает страницу Books'''
        books_link = self.find_element(MainPageLocators.BOOKS_PAGE_LOCATOR)
        books_link.click()
        return BooksPage(self.driver)
