from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK_LOCATORS = (By.CSS_SELECTOR, "#login_link")
    BOOK_LINK_LOCATORS = (By.CSS_SELECTOR, ".dropdown-submenu > a:nth-child(1)")
    ALL_PRODUCTS_LINK_LOCATORS = (By.XPATH, "//*[@id='browse']/li/ul/li[1]/a")
    CLOTHING_LINK_LOCATORS = (By.XPATH, "//*[@id='browse']/li/ul/li[3]/a")
    OFFERS_LINK_LOCATORS = (By.XPATH, '//*[@id="browse"]/li/ul/li[6]/a')
    SEARCH_FIELD_LOCATORS = (By.CSS_SELECTOR, 'input#id_q.form-control')
    SEARCH_BUTTON_LOCATOR = (By.CSS_SELECTOR, 'input.btn.btn-default')
    VIEW_BASKET_BUTTON_LOCATOR = (By.CSS_SELECTOR, '.btn-group > a')
    # BASKET_TOTAL_SUM_LOCATOR = (By.CSS_SELECTOR, 'div.basket-mini.pull-right.hidden-xs > strong#text')
    # BASKET_TOTAL_SUM_LOCATOR2 = (By.CSS_SELECTOR, 'div.basket-mini.pull-right.hidden-xs>strong')
    # BASKET_TOTAL_SUM_LOCATOR3 = (By.XPATH, '//strong[.="Basket total:"]/following-sibling::text()[1]')
    LANGUAGE_BUTTON_GO_LOCATOR = (By.CSS_SELECTOR, 'button.btn:nth-child(4)')
    LANGUAGE_MENU_LOCATOR = (By.CSS_SELECTOR, '.select.form-control')
    ADD_FIRST_BOOK_TO_BASKET = (By.CSS_SELECTOR, '#promotions > section:nth-child(3) > ul > '
                                                 'li:nth-child(1) > article > div.product_price > form > button')
    BOOK_WAS_ADDED = (By.CSS_SELECTOR, 'div.alert:nth-child(3) > div:nth-child(2) > p:first-child')
