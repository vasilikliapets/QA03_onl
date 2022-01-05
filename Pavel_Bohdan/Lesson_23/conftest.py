from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import pytest


@pytest.fixture
def browser():
    browser = webdriver.Firefox()
    yield browser
    browser.implicitly_wait(15)
    browser.quit()
