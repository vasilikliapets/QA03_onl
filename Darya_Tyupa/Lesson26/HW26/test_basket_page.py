from HW26.pages.main_page import MainPage


def test_empty_basket_positive(driver):
    page = MainPage(driver)
    page.open()
    basket_page = page.open_basket_page()
    assert 'Your basket is empty' in basket_page.get_empty_text().text


def test_empty_basket_negative(driver):
    page = MainPage(driver)
    page.open()
    basket_page = page.open_basket_page()
    assert basket_page.get_order_area() is None
