from pages.main_page import MainPage
from pages.books_page import BooksPage
from pages.fiction_page import FictionPage
from pages.basket_page import BasketPage


def test_open_main_pages(driver):
    '''Тест для проверки открытия основной страницы'''
    main_page = MainPage(driver)
    main_page.open()
    assert driver.title == MainPage.TITLE


def test_open_fiction_page(driver):
    '''Тест для проверки перехода с основной страницы на страницу Fiction'''
    main_page = MainPage(driver)
    main_page.open()
    fiction_page = main_page.open_fiction_page()
    assert driver.title == FictionPage.TITLE


def test_open_books_page(driver):
    '''Тест для проверки перехода с основной страницы на страницу Books'''
    main_page = MainPage(driver)
    main_page.open()
    books_page = main_page.open_books_page()
    assert driver.title == BooksPage.TITLE


def test_open_basket_page(driver):
    '''Тест для проверки перехода с основной страницы на страницу Basket'''
    main_page = MainPage(driver)
    main_page.open()
    basket_page = main_page.open_basket_page()
    assert driver.title == BasketPage.TITLE
