from selenium.webdriver.common.by import By

'''Файл с локаторами на страницу Books'''

class BooksPageLocators:
    BOOK_NAME_LOCATOR = (By.XPATH, '//div[@class="col-sm-6 product_main"]/h1')
    BOOK_PICTURE_LOCATOR = (By.CSS_SELECTOR, '.item > img:nth-child(1)')