from selenium.webdriver.common.by import By


class BasketPageLocators:
    BASKET_TITLE_LOCATOR = (By.XPATH, "//*[@class='page-header action']//h1")
    EMPTY_TEXT_LOCATOR = (By.XPATH, "//*[@id='content_inner']//p")
    ORDER_AREA_LOCATOR = (By.XPATH, "//*[@class='basket_summary']")

