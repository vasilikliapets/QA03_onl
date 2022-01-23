from eugene_shurpach.Lesson26.homework26.constants import LOGIN_INCORRECT, PASS_INCORRECT
from eugene_shurpach.Lesson26.homework26.tools.base_page import BasePage
from eugene_shurpach.Lesson26.homework26.tools.login_page_locators import LoginPageLocators


class LoginPage(BasePage):

    def get_title(self):
        return self.driver.title

    def get_oops(self):
        return self.find_element(LoginPageLocators.OOPS_LOCATOR)

    def get_login_form(self):
        return self.find_element(LoginPageLocators.LOGIN_FORM_LOCATORS)

    def get_register_form(self):
        return self.find_element(LoginPageLocators.REGISTER_FORM_LOCATORS)

    def try_to_login(self):
        email = self.find_element(LoginPageLocators.EMAIL_LOCATOR)
        email.send_keys(LOGIN_INCORRECT)
        password = self.find_element(LoginPageLocators.PASSWORD_LOCATOR)
        password.send_keys(PASS_INCORRECT)
        button = self.find_element(LoginPageLocators.BUTTON_LOGIN_LOCATOR)
        button.click()

