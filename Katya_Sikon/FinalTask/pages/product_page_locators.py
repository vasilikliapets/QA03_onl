from selenium.webdriver.common.by import By


class ProductPageLocators:
    ADD_TO_COUNT_LOCATOR = (By.XPATH, '//*[@name="quantity"]')
    ADD_TO_CART_BUTTON_LOCATOR = (By.XPATH, '//button[@name="add_cart_product"]')
    OPEN_CART = (By.CSS_SELECTOR, 'span.quantity')
    ONE_COST = (By.CSS_SELECTOR, 'span.price')

