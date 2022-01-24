from selenium.webdriver.common.by import By


class BasketPageLocators:
    HEADER_BASKET = (By.CSS_SELECTOR, '.page-header.action > h1')
    BASKET_IS_EMPTY = (By.XPATH, '//*[@id="content_inner"]/p')
    CONTINUE_SHOPPING_LINK = (By.CSS_SELECTOR, '#content_inner > p > a')
    PROCEED_TO_CHECKOUT_BTN = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-block")
