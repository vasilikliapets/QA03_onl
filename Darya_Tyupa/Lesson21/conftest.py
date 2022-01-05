import pytest
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By


@pytest.fixture()
def firefox_driver():
    return Firefox()


@pytest.fixture
def login_page(firefox_driver):
    firefox_driver.get('http://the-internet.herokuapp.com/login')
    yield firefox_driver
    firefox_driver.quit()


@pytest.fixture()
def main_page(firefox_driver):
    firefox_driver.get('http://the-internet.herokuapp.com/')
    yield firefox_driver
    firefox_driver.quit()


@pytest.fixture()
def checkbox_page(main_page):
    checkbox_link = main_page.find_element(By.XPATH, "//a[@href='/checkboxes']")
    checkbox_link.click()
    yield main_page


@pytest.fixture()
def multiple_window_page(main_page):
    window_link = main_page.find_element(By.XPATH, "//a[@href='/windows']")
    window_link.click()
    yield main_page


@pytest.fixture()
def add_element_page(main_page):
    elements_link = main_page.find_element(By.XPATH, '//a[@href="/add_remove_elements/"]')
    elements_link.click()
    yield main_page
