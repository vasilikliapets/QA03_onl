from Lesson26.hm26_page_obj.constants import BOOK_SEARCH
from Lesson26.hm26_page_obj.hm26_pages.main_page import MainPage


def test_books_page(driver):
    page = MainPage(driver)
    page.open()
    books_page = page.open_books_page()
    assert books_page.get_books_header().text == 'Books', "Oops, it wasn't Books page"


def test_search_book(driver):
    page = MainPage(driver)
    page.open()
    books_page = page.open_books_page()
    search_page = books_page.open_search_book(BOOK_SEARCH)
    search_page.open_image_book()
    assert BOOK_SEARCH in search_page.get_title()
