import pytest
from selenium.webdriver import Firefox


@pytest.fixture(scope='session')
def firefox_driver():
    return Firefox()


@pytest.fixture(scope='module')
def controls_page(firefox_driver):
    firefox_driver.implicitly_wait(15)
    firefox_driver.get("http://the-internet.herokuapp.com/dynamic_controls")
    yield firefox_driver


@pytest.fixture(scope='module')
def frames_page(firefox_driver):
    firefox_driver.implicitly_wait(15)
    firefox_driver.get("http://the-internet.herokuapp.com/frames")
    yield firefox_driver
    firefox_driver.quit()
