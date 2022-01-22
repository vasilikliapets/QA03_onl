from pages.base_page import BasePage
from pages.basket_page_locators import BasketPageLocators

'''Файл с описанием страницы Basket'''


class BasketPage(BasePage):
    URL = 'http://selenium1py.pythonanywhere.com/en-gb/basket/'
    TITLE = 'Basket | Oscar - Sandbox'

    def __init__(self, driver):
        super().__init__(driver, self.URL)

    def basket_is_empty(self):
        '''Функция находит и возвращает запись о том, что корзина пуста'''
        return self.find_element(BasketPageLocators.BASKET_IS_EMPTY_LOCATORS).text
