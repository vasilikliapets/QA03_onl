from selenium.webdriver.common.by import By


class SearchPageLocators:
    BOOK_IMAGE_LOCATOR = (By.XPATH, "//img[@class='thumbnail']")
    FOUND_BOOK_NAME_LOCATOR = (By.XPATH, "//*[@class='col-sm-6 product_main']")
    FOUND_BOOK_IMAGE_LOCATOR = (By.XPATH, "//*[@src='/media/cache/23/b5/23b50dcbd7ae7bf2c35c1dbe363fee36.jpg']")
