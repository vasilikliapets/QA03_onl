import pytest
from selenium.webdriver.common.by import By

# Positive and Negative name and passw
name_succs = "tomsmith"
passw_succs = "SuperSecretPassword!"
name_fail = "as"
passw_fail = "123!"


def test_registration_success(login_page_driver):
    username_line1 = login_page_driver.find_element(By.ID, 'username')
    username_line1.send_keys(name_succs)
    password_lin2 = login_page_driver.find_element(By.ID, "password")
    password_lin2.send_keys(passw_succs)
    button_login = login_page_driver.find_element(By.XPATH, '//*[@id="login"]/button/i')
    button_login.click()
    log_success = login_page_driver.find_element(By.XPATH, '//*[@id="flash"]')
    assert log_success.text in ("You logged into a secure area!\n×")


def test_registration_fail(login_page_driver):
    username_line1 = login_page_driver.find_element(By.ID, 'username')
    username_line1.send_keys(name_fail)
    password_lin2 = login_page_driver.find_element(By.ID, "password")
    password_lin2.send_keys(passw_fail)
    button_login = login_page_driver.find_element(By.XPATH, '//*[@id="login"]/button/i')
    button_login.click()
    log_fail = login_page_driver.find_element(By.XPATH, '//*[@id="flash"]')
    assert log_fail.text in ("Your username is invalid!\n×")


def test_checkboxes_1(main_page_driver):  # create 2 test for checkbox
    checkboxes_link = main_page_driver.find_element(By.XPATH, '//*[@id="content"]/ul/li[6]/a')
    checkboxes_link.click()
    checkbox1 = main_page_driver.find_element(By.XPATH, '//*[@id="checkboxes"]/input[1]')
    checkbox1.click()
    assert checkbox1.is_selected()


def test_checkboxes_2(main_page_driver):
    checkboxes_link = main_page_driver.find_element(By.XPATH, '//*[@id="content"]/ul/li[6]/a')
    checkboxes_link.click()
    checkbox2 = main_page_driver.find_element(By.XPATH, '//*[@id="checkboxes"]/input[2]')
    checkbox2.click()
    assert checkbox2.is_selected() is False


def test_mult_new_windows(main_page_driver):
    mult_windows = main_page_driver.find_element(By.XPATH, '//*[@id="content"]/ul/li[33]/a')
    mult_windows.click()
    btn_in_mult_windows = main_page_driver.find_element(By.XPATH, '//*[@id="content"]/div/a')
    btn_in_mult_windows.click()
    if len(main_page_driver.window_handles) > 1:
        main_page_driver.switch_to.window(main_page_driver.window_handles[1])
    assert main_page_driver.title in ("New Window")


@pytest.mark.parametrize('element', [3])
def test_add_elem(element, main_page_driver):
    add_remove_elem_link = main_page_driver.find_element(By.XPATH, '//*[@id="content"]/ul/li[2]/a')
    add_remove_elem_link.click()
    btn_add_elem = main_page_driver.find_element(By.XPATH, '//*[@id="content"]/div/button')
    count = 0
    while count != element:
        btn_add_elem.click()
        count += 1
    list_del_btns = main_page_driver.find_elements(By.XPATH, '//*[@id="elements"]/button')  # класс с кнопками
    assert len(list_del_btns) == count


@pytest.mark.parametrize('element', [3])
def test_del_elem(element, main_page_driver):
    add_remove_elem_link = main_page_driver.find_element(By.XPATH, '//*[@id="content"]/ul/li[2]/a')
    add_remove_elem_link.click()
    btn_add_elem = main_page_driver.find_element(By.XPATH, '//*[@id="content"]/div/button')
    count = 0
    while count != element:
        btn_add_elem.click()
        count += 1
    # btn_delete = main_page_driver.find_element(By.XPATH, '//*[@id="elements"]/button')#1 вариант
    btn_delete = main_page_driver.find_element(By.CSS_SELECTOR, '.added-manually:last-child')  # 2 вариант
    btn_delete.click()
    # list_del_btns = main_page_driver.find_elements(By.XPATH, '//button[@class="added-manually"]')#1 Вариант
    list_del_btns = main_page_driver.find_elements(By.XPATH, '//*[@id="elements"]/button')  # 2 Вариант
    assert len(list_del_btns) == count - 1
