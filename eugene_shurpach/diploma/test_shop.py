from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from eugene_shurpach.diploma.tools.constants import USER_EMAIL, COUNT
from eugene_shurpach.diploma.tools.db_steps import LitecartDB
from eugene_shurpach.diploma.tools.main_page import MainPage
from eugene_shurpach.diploma.tools.main_page_locators import MainPageLocators

import allure


@allure.story("Check order ducks")
def test_order(driver):
    """Тест проверяет процесс заказа с количеством из константы COUNT"""
    with allure.step('Open main page'):
        main_page = MainPage(driver)
    with allure.step('Login user'):
        main_page.login_user()
    with allure.step('Open page ducks'):
        ducks_page = main_page.open_ducks_page()
    with allure.step('Open page blue ducks'):
        blue_duck_page = ducks_page.open_blue_duck_page()
    with allure.step('Get price for duck'):
        price_for_duck = blue_duck_page.get_price()
    with allure.step('Add duck in basket'):
        blue_duck_page.add_duck()
    # ожидание пока утки прогрузятся в корзине и открытие корзины
    WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element(MainPageLocators.BASKET_LOCATORS, COUNT))
    with allure.step('Open basket page'):
        basket_page = main_page.open_basket_page()
    with allure.step('Get and check price for duck'):
        unit_cost = basket_page.get_unit_cost()  # получение цены за единицу для проверки правильности
        assert price_for_duck == unit_cost, 'Error price in basket'
    with allure.step('Get and check total price'):
        total_cost = basket_page.get_total_cost()
        assert unit_cost * int(COUNT) == total_cost, 'Error total'
    with allure.step('Confirm order and check success'):
        order_page = basket_page.confirm_order()
        assert order_page.check_success_order(), 'Error by order'


@allure.story("Check order in database")
def test_order_db(db_connect):
    with allure.step('Get order data'):
        order_id = LitecartDB.find_order_id_by_user_email(db_connect, USER_EMAIL)
    with allure.step('Check order in database'):
        assert len(order_id) == 1, 'Order does not exist'
    with allure.step("Delete order"):
        # удаление записи с заказом, чтобы можно было повторно запустить тесты скоупом
       LitecartDB.delete_order_by_user_email(db_connect, USER_EMAIL)
