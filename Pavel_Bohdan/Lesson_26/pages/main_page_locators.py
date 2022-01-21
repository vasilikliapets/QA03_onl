from selenium.webdriver.common.by import By

'''Файл с локаторами на основной странице'''

class MainPageLocators:
    BASKET_LINK_LOCATORS = (By.CSS_SELECTOR, '.btn-group > a')
    SUBMENU_LINK_LOCATORS = (
        By.XPATH, '//li[@class="dropdown-submenu"]')
    BOOKS_PAGE_LOCATOR = (
        By.XPATH, '//a[@href="/en-gb/catalogue/category/books_2/"]')
    BOOKS_LINK_LOCATORS = (
        By.XPATH, '//a[@href="/en-gb/catalogue/category/books_2/"]/strong')
    FICTION_LINK_LOCATORS = (
        By.CSS_SELECTOR, '.nav-list > li:nth-child(2) > ul:nth-child(2) > li:nth-child(1) > a:nth-child(1)')
    SEARCH_FIELD_LOCATORS = (By.XPATH, '//input[@type="search"]')
