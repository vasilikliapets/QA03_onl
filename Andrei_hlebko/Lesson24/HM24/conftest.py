import pytest
from selenium.webdriver import Chrome


@pytest.fixture(scope="session")
def chrome_driver():
    return Chrome()


@pytest.fixture(scope="module")
def heroku_checkbox_dynamic(chrome_driver):
    chrome_driver.get("http://the-internet.herokuapp.com/dynamic_controls")
    chrome_driver.implicitly_wait(5)
    yield chrome_driver
    chrome_driver.close()


@pytest.fixture(scope="module")
def heroku_frames_page(chrome_driver):
    chrome_driver.get("http://the-internet.herokuapp.com/frames")
    chrome_driver.implicitly_wait(5)
    yield chrome_driver
    chrome_driver.close()
