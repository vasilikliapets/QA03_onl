from selenium.webdriver.common.by import By


class MainPageLocators:
    EMAIL_INPUT_LOCATORS = (By.CSS_SELECTOR, 'input[type=text]')
    PASSWORD_INPUT_LOCATORS = (By.CSS_SELECTOR, ' input[type=password]')
    LOGIN_BUTTON_LOCATORS = (By.CSS_SELECTOR, 'button[name=login]')
    BASKET_LOCATORS = (By.XPATH, '//*[@id="cart"]/a[2]')
    CATEGORIES_LOCATORS = (By.LINK_TEXT, 'Rubber Ducks')
