from selenium.webdriver.common.by import By


class BooksPageLocators:
    HEADER_LOCATORS = (By.CSS_SELECTOR, "div.page-header.action > h1")
    SITE_TREE_LOCATORS = (By.CSS_SELECTOR, "ul.breadcrumb > li.active")
    FICTION_LOCATORS = (By.XPATH, "//*[@id='default']/div[2]/div/div/aside/div[2]/ul/li[2]/ul/li[1]/a")
