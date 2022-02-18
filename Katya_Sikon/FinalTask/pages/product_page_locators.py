from selenium.webdriver.common.by import By


class ProductPageLocators:
    ADD_TO_CART_BUTTON_LOCATOR = (By.XPATH, '//button[@name="add_cart_product"]')
    QUANTITY_LOCATOR = (By.XPATH, '//*[name="quantity"]')