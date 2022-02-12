from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from eugene_shurpach.Final_task.tools.main_page import MainPage
from eugene_shurpach.Final_task.tools.main_page_locators import MainPageLocators
import mysql.connector as mysql

db = mysql.connect(
    host='localhost',
    user='root',
    database='litecart')


def test_1(driver, quantity='3'):
    main_page = MainPage(driver)
    main_page.login_user()
    ducks_page = main_page.open_ducks_page()
    blue_duck_page = ducks_page.open_blue_duck_page()
    price_for_duck = blue_duck_page.get_price()
    blue_duck_page.add_duck(quantity)
    WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element(MainPageLocators.BASKET_LOCATORS, quantity))
    basket_page = main_page.open_basket_page()
    unit_cost = basket_page.get_unit_cost()
    assert price_for_duck == unit_cost, 'Error price in basket'
    total_cost = basket_page.get_total_cost()
    assert unit_cost * int(quantity) == total_cost, 'Error total'
    order_page = basket_page.confirm_order()
    assert order_page.check_success_order()


def test_order_db():
    cursor = db.cursor()
    query = "SELECT * FROM `lc_orders` WHERE customer_email='terry1408@yandex.ru' AND date_created >= CURRENT_DATE"
    cursor.execute(query)
    order = cursor.fetchall()
    assert order, 'Order does not exist'
