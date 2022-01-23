from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK_LOCATORS = (By.CSS_SELECTOR, "#login_link")
    OSCAR_REF_LOCATORS = (By.CSS_SELECTOR, 'div[href="/en-gb/"]')
    BOOKS_REF_LOCATORS = (By.CSS_SELECTOR, 'a[href="/en-gb/catalogue/category/books_2/"]')
    BASKET_LOCATORS = (By.XPATH, '//*[@id="default"]/header/div[1]/div/div[2]/span/a')
