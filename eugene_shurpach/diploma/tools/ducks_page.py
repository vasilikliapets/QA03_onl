from eugene_shurpach.diploma.tools.base_page import BasePage
from eugene_shurpach.diploma.tools.duck_page import DuckPage
from eugene_shurpach.diploma.tools.ducks_page_locators import DucksPageLocators


class DucksPage(BasePage):

    def open_yellow_duck_page(self):
        el = self.find_element(DucksPageLocators.YELLOW_DUCK_LOCATOR)
        el.click()
        return DuckPage(self.driver, self.driver.current_url)

    def open_purple_duck_page(self):
        el = self.find_element(DucksPageLocators.PURPLE_DUCK_LOCATOR)
        el.click()
        return DuckPage(self.driver, self.driver.current_url)

    def open_green_duck_page(self):
        el = self.find_element(DucksPageLocators.GREEN_DUCK_LOCATOR)
        el.click()
        return DuckPage(self.driver, self.driver.current_url)

    def open_red_duck_page(self):
        el = self.find_element(DucksPageLocators.RED_DUCK_LOCATOR)
        el.click()
        return DuckPage(self.driver, self.driver.current_url)

    def open_blue_duck_page(self):
        el = self.find_element(DucksPageLocators.BLUE_DUCK_LOCATOR)
        el.click()
        return DuckPage(self.driver, self.driver.current_url)
