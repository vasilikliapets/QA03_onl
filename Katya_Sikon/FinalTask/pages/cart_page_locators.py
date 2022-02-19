from selenium.webdriver.common.by import By


class CartPageLocators:
    CONFIRM_ORDER_LOCATOR = (By.XPATH, '//*[@name="confirm_order"]')
    TOTAL_COST_LOCATOR = (By.CSS_SELECTOR, 'td.sum')
    BOX_CART_LOCATOR = (By.XPATH, '//*[@id="box-checkout-cart"]')


