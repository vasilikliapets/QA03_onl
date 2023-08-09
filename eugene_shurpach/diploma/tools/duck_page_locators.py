from selenium.webdriver.common.by import By


class DuckPageLocators:
    PRICE = (By.CSS_SELECTOR, '.price[itemprop="price"]')
    BUTTON_ADD = (By.CSS_SELECTOR, 'button[type="submit"]')
    INPUT_QUANTITY = (By.CSS_SELECTOR, 'input[type="number"]')
