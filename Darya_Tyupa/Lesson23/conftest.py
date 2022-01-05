import pytest
from selenium.webdriver import Firefox


@pytest.fixture()
def firefox_driver():
    return Firefox()


@pytest.fixture()
def forms_page(firefox_driver):
    firefox_driver.implicitly_wait(15)
    firefox_driver.get('https://ultimateqa.com/filling-out-forms/')
    yield firefox_driver
    firefox_driver.quit()
