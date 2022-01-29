from selenium.webdriver.common.by import By


class BasketPageLocators:
    HEADER_LOCATORS = (By.CSS_SELECTOR, "div.page-header.action > h1")
    EMPTY_LOCATORS = (By.CSS_SELECTOR, "#content_inner")
