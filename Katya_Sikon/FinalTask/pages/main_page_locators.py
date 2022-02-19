from selenium.webdriver.common.by import By


class MainPageLocators:
    EMAIL_LOCATOR = (By.XPATH, '//*[@name="email"]')
    PASSWORD_LOCATOR = (By.XPATH, '//*[@name="password"]')
    LOGIN_BUTTON_LOCATOR = (By.XPATH, '//button[@name="login"]')
    GREEN_DUCK_LOCATOR = (By.XPATH, '//*[@title="Green Duck"]')
    CART_LOCATOR = (By.XPATH, 'span.quantity')
