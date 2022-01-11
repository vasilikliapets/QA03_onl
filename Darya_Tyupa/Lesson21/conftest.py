import pytest
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By


@pytest.fixture(scope='session')
def firefox_driver():
    return Firefox()


@pytest.fixture
def login_page(firefox_driver):
    firefox_driver.get('http://the-internet.herokuapp.com/login')
    yield firefox_driver


@pytest.fixture(scope='module')
def checkbox_page(firefox_driver):
    firefox_driver.get('http://the-internet.herokuapp.com/')
    checkbox_link = firefox_driver.find_element(By.XPATH, "//a[@href='/checkboxes']")
    checkbox_link.click()
    yield firefox_driver


@pytest.fixture()
def add_element_page(firefox_driver):
    firefox_driver.get('http://the-internet.herokuapp.com/')
    elements_link = firefox_driver.find_element(By.XPATH, '//a[@href="/add_remove_elements/"]')
    elements_link.click()
    yield firefox_driver


@pytest.fixture()
def multiple_window_page(firefox_driver):
    firefox_driver.get('http://the-internet.herokuapp.com/')
    window_link = firefox_driver.find_element(By.XPATH, "//a[@href='/windows']")
    window_link.click()
    yield firefox_driver
    firefox_driver.quit()
