import pytest
from selenium.webdriver import Firefox


@pytest.fixture(scope='session')
def firefox_driver():
    return Firefox()

#  из-за того что тесты требовали возвращения на исходную страницу, если поставить закрытие
#  браузера в фикстуру ниже, то браузер закрывался и открывался бы на каждом тесте.
#  Поэтому я сделала отдельную фикстуру на закрытие браузера
@pytest.fixture(scope='session')
def quit_driver(firefox_driver):
    yield firefox_driver
    firefox_driver.quit()


@pytest.fixture()
def forms_page(quit_driver):
    quit_driver.implicitly_wait(15)
    quit_driver.get('https://ultimateqa.com/filling-out-forms/')
    yield quit_driver
