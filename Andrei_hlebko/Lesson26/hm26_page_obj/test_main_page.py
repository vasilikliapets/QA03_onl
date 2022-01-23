from Lesson26.hm26_page_obj.hm26_pages.main_page import MainPage


def test_main_page(driver):
    """
    The test check do we have a login form and title
    """
    page = MainPage(driver)
    page.open()
    login_page = page.open_login_page()
    assert login_page.get_login_form().is_displayed(), "Login form doesn't exist"
    assert 'Login' in login_page.get_title(), "Title doesn't exist"


def test_incorrect_login(driver):
    """
    The test check login with wrong param
    """
    page = MainPage(driver)
    page.open()
    login_page = page.open_login_page()
    assert "Oops! We found some errors" in login_page.get_oops(), "Oops message doesn't exist"

def test_open_and_check_empty_basket(driver):
    """
    The test,we are switching from main page to basket page,and checking our basket empty or not
    """
    page = MainPage(driver)
    page.open()
    basket_page = page.open_basket_page()
    assert "Your basket is empty" in basket_page.check_basket_empty().text, "Opps message doesn't exist"


def test_open_and_check_fiction_page(driver):
    """
    The test, we are switching from main page to fiction page, and checking on the right page or not
    """
    page = MainPage(driver)
    page.open()
    fiction_page = page.open_books_fiction_page()
    assert "Fiction" in fiction_page.get_fiction_page_header().text, "Opps message doesn't exist"
