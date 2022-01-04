import pytest
from selenium.webdriver import Chrome


@pytest.fixture()
def chrome_driver():
    return Chrome()


@pytest.fixture()
def main_link_swag(chrome_driver):
    chrome_driver.get("https://www.saucedemo.com/")
    chrome_driver.implicitly_wait(5)
    yield chrome_driver
    chrome_driver.close()
