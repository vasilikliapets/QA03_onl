from selenium.webdriver.common.by import By


class BasketPageLocators:
    DUCKS_IN_BASKET = (By.CSS_SELECTOR, 'td.item')
    TOTAL = (By.CSS_SELECTOR, 'td.sum')
    UNIT_COST = (By.CSS_SELECTOR, 'td.unit-cost')
    CONFIRM_BUTTON = (By.CSS_SELECTOR, 'button[value="Confirm Order"]')
    ITEMS_LOCATORS = (By.ID, 'box-checkout-cart')
