from HW26.constans import BOOK_CODERS_AT_WORK
from HW26.pages.main_page import MainPage



def test_redirection_to_login_page(driver):
    page = MainPage(driver)
    page.open()
    login_page = page.open_login_page()
    assert login_page.get_login_form().is_displayed(), "Login form doesn't exist"
    assert 'Login' in login_page.get_title(), "Title isn't wright"


def test_redirection_to_books_page(driver):
    page = MainPage(driver)
    page.open()
    books_page = page.open_books_page()
    assert 'Books' in books_page.get_books_page_title().text


def test_redirection_to_basket_page(driver):
    page = MainPage(driver)
    page.open()
    basket_page = page.open_basket_page()
    assert 'Basket' in basket_page.get_basket_page_title().text



def test_redirection_to_fiction(driver):
    page = MainPage(driver)
    page.open()
    books_page = page.open_books_page()
    fiction_page = books_page.open_fiction_page()
    assert 'Fiction' in fiction_page.get_fiction_page_title()








