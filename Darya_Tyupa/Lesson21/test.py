import time

import pytest
from selenium.webdriver.common.by import By


def test_successful_login(login_page):
    """This test checks the message of successful login"""
    username_field = login_page.find_element(By.ID, "username")
    username_field.send_keys("tomsmith")
    password_field = login_page.find_element(By.ID, "password")
    password_field.send_keys("SuperSecretPassword!")
    login_btn = login_page.find_element(By.CSS_SELECTOR, 'button.radius')
    login_page.implicitly_wait(15)
    login_btn.click()
    message_success = login_page.find_element(By.XPATH, "//div[@id='flash' and @class='flash success']")
    assert message_success.is_displayed()


def test_unsuccessful_login(login_page):
    """This test checks the message of failed login"""
    username_field = login_page.find_element(By.ID, "username")
    username_field.send_keys("dasha")
    password_field = login_page.find_element(By.ID, "password")
    password_field.send_keys("66699993!D")
    login_btn = login_page.find_element(By.CSS_SELECTOR, 'button.radius')
    login_page.implicitly_wait(15)
    login_btn.click()
    message_error = login_page.find_element(By.XPATH, "//div[@id='flash' and @class='flash error']")
    assert message_error.is_displayed()


def test_setting_check_mark(checkbox_page):
    """This test checks the setting of checkmark"""
    checkbox_1 = checkbox_page.find_element(By.XPATH, "//input[1][@type='checkbox']")
    checkbox_1.click()
    assert checkbox_1.is_selected()


def test_unchecking(checkbox_page):
    """This test checks the unchecking of checkmark"""
    checkbox_2 = checkbox_page.find_element(By.XPATH, "//input[2][@type='checkbox']")
    checkbox_2.click()
    assert checkbox_2.is_selected() is False


def test_new_window(multiple_window_page):
    """This test checks the opening the new window"""
    click_link = multiple_window_page.find_element(By.LINK_TEXT, "Click Here")
    click_link.click()
    time.sleep(3)
    main_window = multiple_window_page.current_window_handle
    new_window = [window for window in multiple_window_page.window_handles if window != main_window][0]
    multiple_window_page.switch_to.window(new_window)
    assert multiple_window_page.title == 'New Window'


@pytest.mark.parametrize('number', [1, 2, 3])
def test_add_elements(number, add_element_page):
    """This test checks the adding element(s)"""
    add_button = add_element_page.find_element(By.XPATH, '//button[@onclick="addElement()"]')
    repeat = 0
    while repeat != number:
        add_button.click()
        repeat += 1
    assert number == len(add_element_page.find_elements(By.XPATH, '//button[@class="added-manually"]'))


@pytest.mark.parametrize('number', [1, 2, 3])
def test_remove_element(number, add_element_page):
    """This test checks the deleting element(s)"""
    add_button = add_element_page.find_element(By.XPATH, '//button[@onclick="addElement()"]')
    repeat = 0
    while repeat != number:
        add_button.click()
        repeat += 1
    delete_button = add_element_page.find_element(By.XPATH, '//button[@class="added-manually"]')
    delete_button.click()
    number_of_buttons = add_element_page.find_elements(By.XPATH, '//button[@class="added-manually"]')
    assert len(number_of_buttons) == number - 1
