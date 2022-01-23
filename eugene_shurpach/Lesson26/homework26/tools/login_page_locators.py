from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_FORM_LOCATORS = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM_LOCATORS = (By.CSS_SELECTOR, '#register_form')
    EMAIL_LOCATOR = (By.XPATH, '//*[@id="id_login-username"]')
    PASSWORD_LOCATOR = (By.XPATH, '//*[@id="id_login-password"]')
    BUTTON_LOGIN_LOCATOR = (By.XPATH, '//button[@name="login_submit"]')
    OOPS_LOCATOR = (By.XPATH, '//*[@class="alert alert-danger"][1]//strong')
