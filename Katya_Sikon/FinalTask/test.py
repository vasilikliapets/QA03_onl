from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from constants import COUNT,EMAIL
from pages.main_page import MainPage
from pages.product_page_locators import ProductPageLocators

import mysql.connector as mysql

db = mysql.connect(
    host="localhost",
    user="root",
    database="litecart"
)

cursor = db.cursor()


def test_cart(driver):
    page = MainPage(driver)
    page.login()
    page_duck = page.choose_green_duck()
    cost_duck = page_duck.get_cost()
    page_duck.add_to_cart()
    WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element(ProductPageLocators.OPEN_CART, str(COUNT)))
    # не пойдет дальше пока утки не добавлены
    page_cart = page_duck.open_cart()
    page_cart_duck = page_cart.duck_in_cart()
    total_cost = page_cart.get_total_cost()
    page_cart.confirm_order()
    assert page_cart_duck, "Ducks is upsent"
    assert cost_duck * COUNT == total_cost, 'Incorrect price in the cart'


def test_order():
    cursor.execute(f"SELECT date_created FROM lc_orders WHERE customer_email = '{EMAIL}' and date_created >= SUBTIME("
                   f"NOW(),'0:2:0.000000')")
    date_created = cursor.fetchall()
    assert len(date_created) == 1, 'No order'