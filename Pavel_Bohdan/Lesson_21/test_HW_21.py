from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import pytest


@pytest.mark.parametrize('login, password', [('tomsmith', 'SuperSecretPassword!'), pytest.param('sam', 'password', marks=pytest.mark.xfail)])
def test_smith(browser, login, password):

    browser.get('http://the-internet.herokuapp.com/login')

    name = browser.find_element(By.XPATH, '//*[@id="username"]')
    name.send_keys(login)

    passwd = browser.find_element(By.XPATH, '//*[@id="password"]')
    passwd.send_keys(password)

    login_button = browser.find_element(
        By.XPATH, '//button[@type="submit"]')
    login_button.click()

    access = browser.find_element(By.XPATH, '//div[@id="flash"]')

    assert 'You logged into a secure area!' in access.text


def test_check_box(main_page):

    cb_page = main_page.find_element(By.XPATH, '//a[@href="/checkboxes"]')
    cb_page.click()

    check_box_1 = main_page.find_element(
        By.XPATH, '//input[@type="checkbox"][1]')
    check_box_1.click()

    check_box_2 = main_page.find_element(
        By.XPATH, '//input[@type="checkbox"][2]')
    check_box_2.click()

    assert check_box_1.is_selected() == True
    assert check_box_2.is_selected() == False


def test_mult_window(main_page):

    mult_window = main_page.find_element(By.XPATH, '//a[@href="/windows"]')
    mult_window.click()

    click_here = main_page.find_element(By.XPATH, '//a[@href="/windows/new"]')
    click_here.click()

    new_window = main_page.window_handles[1]
    title = main_page.switch_to.window(new_window)
    title = main_page.title

    assert title == 'New Window'


def test_add_element(main_page):

    add_window = main_page.find_element(
        By.XPATH, '//a[@href="/add_remove_elements/"]')
    add_window.click()

    add_element = main_page.find_element(
        By.XPATH, '//button[@onclick="addElement()"]')
    add_element.click()

    new_element = main_page.find_element(
        By.XPATH, '//button[@class="added-manually"]')

    assert new_element.is_enabled() == True


def test_del_element(main_page):
    try:
        add_window = main_page.find_element(
            By.XPATH, '//a[@href="/add_remove_elements/"]')
        add_window.click()

        add_element = main_page.find_element(
            By.XPATH, '//button[@onclick="addElement()"]')
        add_element.click()

        new_element = main_page.find_element(
            By.XPATH, '//button[@class="added-manually"]')
        new_element.click()

        new_element_exist = main_page.find_element(
            By.XPATH, '//button[@class="added-manually"]')

    except NoSuchElementException:
        new_element_exist = False

    assert new_element_exist == False
