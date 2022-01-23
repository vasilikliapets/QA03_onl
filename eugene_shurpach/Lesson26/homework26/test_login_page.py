from eugene_shurpach.Lesson26.homework26.tools.main_page import MainPage


def test_oscar_ref_exists(driver):
    page = MainPage(driver)
    page.open()
    login_page = page.open_login_page()
    assert login_page.get_login_form(), "Login form exists"
    assert login_page.get_register_form(), "Register form exists"
    assert "Login" in login_page.get_title(), "Incorrect title"


def test_books_is_open(driver):
    page = MainPage(driver)
    page.open()
    books_page = page.open_books_page()
    assert books_page.get_header().text == "Books", "Incorrect header name"
    assert books_page.get_site_tree(), "Tree exists"
    assert books_page.get_site_tree().text == "Books", "Incorrect tree name"
