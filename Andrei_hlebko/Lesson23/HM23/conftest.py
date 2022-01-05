import pytest
from selenium.webdriver import Chrome


@pytest.fixture()
def chrome_driver():
    return Chrome()


@pytest.fixture()
def ultinateqa_complic_page(chrome_driver):
    chrome_driver.get("https://ultimateqa.com/complicated-page/")
    chrome_driver.implicitly_wait(5)
    yield chrome_driver
    chrome_driver.close()


@pytest.fixture()
def ultinateqa_filling_out_forms_page(chrome_driver):
    chrome_driver.get("https://ultimateqa.com/filling-out-forms/")
    chrome_driver.implicitly_wait(5)
    yield chrome_driver
    chrome_driver.close()
