from selenium.webdriver.common.by import By

'''Файл с локаторами на странице поиска'''

class SearchPageLocators:
    BOOKS_LOCATOR = (By.XPATH, '//img[@class="thumbnail"]')
