from selenium.webdriver.common.by import By

class MainPageLocators:
    LOGIN_LINK_LOCATOR = (By.XPATH, "//*[@id='login_link']")
    BOOK_LINK_LOCATOR = (By.XPATH, "//*[@href='/en-gb/catalogue/category/books_2/']")
    BASKET_LINK_LOCATOR = (By.XPATH, "//a[@class='btn btn-default']")
