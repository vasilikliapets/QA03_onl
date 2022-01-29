from eugene_shurpach.Lesson26.homework26.tools.main_page import MainPage


def test_basket_page(driver):
    page = MainPage(driver)
    page.open()
    basket_page = page.open_basket_page()
    assert 'Basket' in basket_page.get_header().text, "Title doesn't contain Basket"


def test_empty_basket(driver):
    page = MainPage(driver)
    page.open()
    basket_page = page.open_basket_page()
    empty_text = basket_page.get_empty_basket()
    assert "Your basket is empty." in empty_text.text
