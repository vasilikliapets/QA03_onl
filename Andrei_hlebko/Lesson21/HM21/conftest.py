import pytest
from selenium.webdriver import Chrome


@pytest.fixture(scope="session")
def chrome_driver():
    return Chrome()


@pytest.fixture(scope='module')
def main_page_driver(chrome_driver):
    chrome_driver.get("http://the-internet.herokuapp.com")
    chrome_driver.implicitly_wait(15)
    yield chrome_driver
    chrome_driver.close()


@pytest.fixture(scope='module')
def login_page_driver(chrome_driver):
    chrome_driver.get("http://the-internet.herokuapp.com/login")
    chrome_driver.implicitly_wait(15)
    yield chrome_driver
    chrome_driver.close()
