from pages.main_page import MainPage
from pages.books_page import BooksPage
from pages.fiction_page import FictionPage
from pages.basket_page import BasketPage
from pages.search_page_locators import SearchPageLocators
from pages.books_page_locators import BooksPageLocators
from constants import BOOK_1


def test_book_name(driver):
    '''Тест для проверки правильности найденной книги'''
    main_page = MainPage(driver)
    main_page.open()
    books_page = main_page.open_books_page()
    book = books_page.find_book_by_name(BOOK_1)
    assert book.find_element(
        BooksPageLocators.BOOK_NAME_LOCATOR).text == BOOK_1


def test_book_image(driver):
    '''Тест для проверки наличия изображения книги на странице с книгой'''
    main_page = MainPage(driver)
    main_page.open()
    books_page = main_page.open_books_page()
    book = books_page.find_book_by_name(BOOK_1)
    assert book.find_element(
        BooksPageLocators.BOOK_PICTURE_LOCATOR).is_enabled()


def test_book_page_title(driver):
    '''Тест для проверки правильности названия найденной книги после её поиска'''
    main_page = MainPage(driver)
    main_page.open()
    books_page = main_page.open_books_page()
    book = books_page.find_book_by_name(BOOK_1)
    assert BOOK_1 in book.get_title()
