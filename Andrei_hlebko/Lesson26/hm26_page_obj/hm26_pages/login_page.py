from Lesson26.constants import LOGIN_INCORRECT, PASS_INCORRECT
from Lesson26.hm26_page_obj.hm26_pages.base_page import BasePage
from Lesson26.hm26_page_obj.hm26_pages.login_page_locators import LoginPageLocators


class LoginPage(BasePage):
    def get_login_form(self):
        """
        The func get login form
        """
        return self.find_element(LoginPageLocators.LOGIN_FORM_LOCATORS)

    def get_register_form(self):
        """
        The func get register form
        """
        return self.find_element(LoginPageLocators.REGISTER_FORM_LOCATORS)

    def get_title(self):
        """
        The func get a title
        """
        return self.driver.title

    def try_to_login(self):
        """
        The func input incorrect login and password in login form
        """
        email = self.find_element(LoginPageLocators.EMAIL_LOCATOR)
        email.send_keys(LOGIN_INCORRECT)
        password = self.find_element(LoginPageLocators.PASSWORD_LOCATOR)
        password.send_keys(PASS_INCORRECT)
        button = self.find_element(LoginPageLocators.BUTTON_LOGIN_LOCATOR)
        button.click()

    def get_oops(self):
        """

        The func get and return message after wrong registration
        """
        return self.find_element(LoginPageLocators.OOPS_LOCATOR)
