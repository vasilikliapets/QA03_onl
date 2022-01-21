from selenium.webdriver.common.by import By


class BookPageLocators:
    TITLE_BOOK_LOCATOR = (By.CSS_SELECTOR, '.page-header > h1:nth-child(1)')  # .page-header > h1   #text Books
    SITE_TREE_LOCATORS = (By.CSS_SELECTOR, "ul.breadcrumb > li.active")
    ALL_SHOWCASE_BOOKS_LOCATOR = (By.CSS_SELECTOR, 'ol.row')
    FICTION_LINK_LOCATOR = (By.CSS_SELECTOR, 'a[href*="/en-gb/catalogue/category/books/fiction_3/"]:nth-last-child(2)')
    COMPUTERS_IN_LITER_LINK_LOCATOR = (By.CSS_SELECTOR,
                                       'a[href*="/en-gb/catalogue/category/books/fiction/computers-in-literature_4/"]')
    NON_FICTION_LINK_LOCATOR = (
        By.CSS_SELECTOR, 'a[href*="/en-gb/catalogue/category/books/non-fiction_5/"]:nth-last-child(2)')
    ESSENTIAL_PROGRAM_LINK_LOCATOR = (
        By.CSS_SELECTOR, 'a[href*="/en-gb/catalogue/category/books/non-fiction/essential-programming_6/"]')
    HACKING_LINK_LOCATOR = (By.CSS_SELECTOR, 'a[href*="/en-gb/catalogue/category/books/non-fiction/hacking_7/"]')
    VIEW_BASKET_LINK_LOCATOR = (By.CSS_SELECTOR, '.btn-group > a')
    INPUT_SEARCH_LOCATORS = (By.CSS_SELECTOR, 'input#id_q.form-control')
    BUTTON_SEARCH_LOCATORS = (By.CSS_SELECTOR, 'input.btn.btn-default')
    CURRENT_PAGE_DOWN_LOCATOR = (By.CSS_SELECTOR, 'li.current')  # Page 1 of 6
    NEXT_PAGE_BTN_LOCATOR = (By.CSS_SELECTOR, '.next > a')  # .next > a:nth-child(1)
