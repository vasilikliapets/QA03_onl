from Lesson26.hm26_page_obj.hm26_pages.main_page import MainPage


def test_basket_page(driver):
    page = MainPage(driver)
    page.open()
    basket_page = page.open_basket_page()
    assert basket_page.get_basket_page_header().text == 'Basket', "Oops it wasn't Basket page"


def test_add_one_book(driver):
    page = MainPage(driver)
    page.open()
    basket_page = page.add_one_book_in_basket()
    assert "Your basket total is now" in basket_page.get_inf_book_was_added().text, "Oops,We can't add book to the basket"


def test_proceed_to_checkout_btn_in_basket(driver):
    """
    The test check button Proceed to checkout in basket is displayed or not after adding a book
    """
    page = MainPage(driver)
    page.open()
    basket_page = page.add_one_book_in_basket_and_switch_to_basket()
    assert basket_page.check_proceed_to_checkout_btn().is_displayed(), "Button Proceed to checkout not displayed"
