from pages.main_page import MainPage


def test_cart(driver):
    page = MainPage(driver)
    page.open() #открыть сайт
    login_user = page.login() #залогиниться
    duck_page = page.choose_green_duck() #выбрать утку
    quantity_duck = duck_page.change_quantity()# изменить количество уток на три
    add_duck_to_cart = duck_page.add_to_cart() #добавить утку в корзину


