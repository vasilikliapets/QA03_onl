from selenium.webdriver.common.by import By

'''Файл с локаторами на странице Basket'''

class BasketPageLocators:
    BASKET_IS_EMPTY_LOCATORS = (
        By.CSS_SELECTOR, '#content_inner > p:nth-child(1)')
