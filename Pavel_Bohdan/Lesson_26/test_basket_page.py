from pages.main_page import MainPage
from pages.main_page_locators import MainPageLocators
from pages.basket_page import BasketPage


def test_basket_is_empty(driver):
    '''Тест проверяющий пуста ли корзина'''
    main_page = MainPage(driver)
    main_page.open()
    basket_page = main_page.open_basket_page()
    empty_basket = basket_page.basket_is_empty()
    assert 'Your basket is empty.' in empty_basket
