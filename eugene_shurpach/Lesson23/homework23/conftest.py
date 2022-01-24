import pytest
from selenium.webdriver import Chrome


@pytest.fixture(scope="session")
def chrome_driver():
    return Chrome()


@pytest.fixture(scope='module')
def page_driver(chrome_driver):
    chrome_driver.get("https://ultimateqa.com/filling-out-forms/")
    yield chrome_driver
    chrome_driver.close()
