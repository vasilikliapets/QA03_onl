from eugene_shurpach.Final_task.tools.duck_page import DuckPage
from eugene_shurpach.Final_task.tools.duck_page_locators import DuckPageLocators
from eugene_shurpach.Final_task.tools.main_page import MainPage


def test_1(driver):
    main_page = MainPage(driver)
    main_page.login_user()
    ducks_page = main_page.open_ducks_page()
    blue_duck_page = ducks_page.open_blue_duck_page()
    price_for_duck = blue_duck_page.get_price()
    blue_duck_page.add_duck("3")
    basket_page = main_page.open_basket_page()
    



