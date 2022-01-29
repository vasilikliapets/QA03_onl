from eugene_shurpach.Lesson26.homework26.tools.main_page import MainPage


def test_main_page(driver):
    page = MainPage(driver)
    page.open()
    login_page = page.open_login_page()
    assert login_page.get_login_form().is_displayed(), "Login form doesn't exist"
    assert 'Login' in login_page.get_title(), "Title doesn't contain Login"


def test_login(driver):
    page = MainPage(driver)
    page.open()
    login_page = page.open_login_page()
    login_page.try_to_login()
    assert login_page.get_oops(), "Oops message doesn't exist"

