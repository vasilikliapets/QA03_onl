import pytest
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.implicitly_wait(15)
    driver.quit()


@pytest.fixture
def main_page(browser):
    browser.get('http://the-internet.herokuapp.com')
    return browser
