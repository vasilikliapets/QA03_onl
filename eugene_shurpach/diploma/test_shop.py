from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from eugene_shurpach.diploma.tools.constants import USER_EMAIL, COUNT
from eugene_shurpach.diploma.tools.main_page import MainPage
from eugene_shurpach.diploma.tools.main_page_locators import MainPageLocators
import mysql.connector as mysql

db = mysql.connect(
    host='localhost',
    user='root',
    database='litecart')
cursor = db.cursor()


def test_order(driver):
    """Тест проверяет процесс заказа с количеством из константы COUNT"""
    main_page = MainPage(driver)
    main_page.login_user()  # авторизация на главное странице
    ducks_page = main_page.open_ducks_page()  # открытие страницы с утками
    blue_duck_page = ducks_page.open_blue_duck_page()  # открытие страницы с голубой уткой
    price_for_duck = blue_duck_page.get_price()  # получение цены для последующих проверок
    blue_duck_page.add_duck()  # добавление уток в корзину
    # ожидание пока утки прогрузятся в корзине и открытие корзины
    WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element(MainPageLocators.BASKET_LOCATORS, COUNT))
    basket_page = main_page.open_basket_page()
    unit_cost = basket_page.get_unit_cost()  # получение цены за единицу для проверки правильности
    assert price_for_duck == unit_cost, 'Error price in basket'
    # получение общей стоимости в корзине
    total_cost = basket_page.get_total_cost()
    # проверка правильности расчета итоговой стоимости
    assert unit_cost * int(COUNT) == total_cost, 'Error total'
    # оформление заказа
    order_page = basket_page.confirm_order()
    # проверка успешности заказа
    assert order_page.check_success_order(), 'Error by order'


def test_order_db():
    cursor.execute(f"SELECT date_created FROM lc_orders WHERE customer_email = '{USER_EMAIL}' "
                   f"AND date_created >= DATE_ADD(NOW(), INTERVAL -215 MINUTE)")
    date_created = cursor.fetchall()
    assert len(date_created) == 1, 'Order does not exist'
    # удаление записи с заказом, чтобы можно было повторно запустить тесты скоупом
    cursor.execute(f"DELETE FROM lc_orders WHERE customer_email = '{USER_EMAIL}' "
                   f"AND date_created >= DATE_ADD(NOW(), INTERVAL -215 MINUTE)")
