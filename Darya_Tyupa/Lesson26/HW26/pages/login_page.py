from HW26.constans import LOGIN_EMAIL, LOGIN_PASSWORD
from HW26.pages.base_page import BasePage
from HW26.pages.login_page_locators import LoginPageLocators


class LoginPage(BasePage):
    def get_login_form(self):
        return self.find_element(LoginPageLocators.LOGIN_FORM_LOCATORS)

    def get_register_form(self):
        return self.find_element(LoginPageLocators.REGISTER_FORM_LOCATORS)

    def get_title(self):
        return self.driver.title

    def try_to_login(self):
        email = self.find_element(LoginPageLocators.EMAIL_LOCATOR)
        email.send_keys(LOGIN_EMAIL)
        password = self.find_element(LoginPageLocators.PASSWORD_LOCATOR)
        password.send_keys(LOGIN_PASSWORD)
        button = self.find_element(LoginPageLocators.BUTTON_LOGIN_LOCATOR)
        button.click()

    def get_oops(self):
        return self.find_element(LoginPageLocators.OOPS_LOCATOR)


