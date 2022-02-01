from HW26.constans import BOOK_CODERS_AT_WORK
from HW26.pages.main_page import MainPage


def test_search_book_title(driver):
    page = MainPage(driver)
    page.open()
    books_page = page.open_books_page()
    search_page = books_page.open_search_book(BOOK_CODERS_AT_WORK)
    search_page.open_image_book()
    assert BOOK_CODERS_AT_WORK in search_page.get_title()


def test_found_book_name(driver):
    page = MainPage(driver)
    page.open()
    books_page = page.open_books_page()
    search_page = books_page.open_search_book(BOOK_CODERS_AT_WORK)
    search_page.open_image_book()
    assert BOOK_CODERS_AT_WORK in search_page.get_found_book_name().text


def test_found_book_image(driver):
    page = MainPage(driver)
    page.open()
    books_page = page.open_books_page()
    search_page = books_page.open_search_book(BOOK_CODERS_AT_WORK)
    search_page.open_image_book()
    assert search_page.get_found_book_image().is_displayed()