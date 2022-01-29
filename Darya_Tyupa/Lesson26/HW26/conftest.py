import pytest
from selenium.webdriver import Firefox

from HW26.pages.main_page import MainPage


@pytest.fixture(scope='session')
def driver():
    driver = Firefox()
    yield driver
    driver.quit()

#TODO
@pytest.fixture()
def main_page(driver):
    page = MainPage(driver)

    page.open()
    return