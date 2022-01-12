import pytest
from selenium.webdriver import Chrome


@pytest.fixture()
def chrome_driver():
    return Chrome()


@pytest.fixture()
def hw21_ex1_driver(chrome_driver):
    chrome_driver.get("http://the-internet.herokuapp.com/login")
    chrome_driver.implicitly_wait(15)
    yield chrome_driver
    chrome_driver.close()


@pytest.fixture()
def hw21_ex2_driver(chrome_driver):
    chrome_driver.get("https://the-internet.herokuapp.com")
    chrome_driver.implicitly_wait(15)
    yield chrome_driver
    chrome_driver.close()
