from selenium.webdriver.common.by import By


class BooksPageLocators:
    BOOKS_TITLE_LOCATOR = (By.XPATH, "//*[@class='page-header action']//h1")
    FICTION_LINK_LOCATOR = (By.XPATH,
                            "//*[@class='side_categories']//a[@href='/en-gb/catalogue/category/books/fiction_3/']")
    SITE_TREE_LOCATORS = (By.CSS_SELECTOR, "ul.breadcrumb > li.active")
    SEARCH_FIELD_LOCATOR = (By.XPATH, "//*[@id='id_q']")
    SEARCH_BUTTON_LOCATOR = (By.XPATH, "//input[@class='btn btn-default']")