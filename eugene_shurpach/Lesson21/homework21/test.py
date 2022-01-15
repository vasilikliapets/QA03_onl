from selenium import webdriver
from selenium.webdriver.common.by import By


def test_login_unsuccess(login_page_driver):
    username = login_page_driver.find_element(By.ID, 'username')
    username.send_keys('admin')
    password = login_page_driver.find_element(By.ID, "password")
    password.send_keys('admin!')
    button_login = login_page_driver.find_element(By.XPATH, '//*[@id="login"]/button/i')
    button_login.click()
    success = login_page_driver.find_element(By.XPATH, '//*[@id="flash"]')
    assert success.text in ('Your username is invalid!\n×')


def test_login_success(login_page_driver):
    username = login_page_driver.find_element(By.ID, 'username')
    username.send_keys('tomsmith')
    password = login_page_driver.find_element(By.ID, "password")
    password.send_keys('SuperSecretPassword!')
    button_login = login_page_driver.find_element(By.XPATH, '//*[@id="login"]/button/i')
    button_login.click()
    success = login_page_driver.find_element(By.XPATH, '//*[@id="flash"]')
    assert success.text in ('You logged into a secure area!\n×')


def test_checkbox_1(main_page_driver):
    checkbox = main_page_driver.find_element(By.LINK_TEXT, 'Checkboxes')
    checkbox.click()
    checkbox_1 = main_page_driver.find_element(By.XPATH, '//*[@id="checkboxes"]/input[1]')
    checkbox_1.click()
    checkbox_2 = main_page_driver.find_element(By.XPATH, '//*[@id="checkboxes"]/input[2]')
    checkbox_2.click()
    assert checkbox_2.is_selected() is False
    assert checkbox_1.is_selected()


def test_add_elem(main_page_driver):
    add_remove_element = main_page_driver.find_element(By.LINK_TEXT, 'Add/Remove Elements')
    add_remove_element.click()
    quantity_elements = len(main_page_driver.find_elements(By.XPATH, '//*[@id="elements"]/button'))
    add_button = main_page_driver.find_element(By.XPATH, '//*[@id="content"]/div/button')
    add_button.click()
    check = len(main_page_driver.find_elements(By.XPATH, '//*[@id="elements"]/button'))
    assert check == quantity_elements + 1


def test_del_elem(main_page_driver):
    del_remove_element = main_page_driver.find_element(By.LINK_TEXT, 'Add/Remove Elements')
    del_remove_element.click()
    add_button = main_page_driver.find_element(By.XPATH, '//*[@id="content"]/div/button')
    add_button.click()
    quantity_elements = len(main_page_driver.find_elements(By.XPATH, '//*[@id="elements"]/button'))
    del_button = main_page_driver.find_element(By.XPATH, '//*[@id="elements"]/button')
    del_button.click()
    assert len(main_page_driver.find_elements(By.XPATH, '//*[@id="elements"]/button')) == quantity_elements - 1


def test_new_windows(main_page_driver):
    multiwindows = main_page_driver.find_element(By.LINK_TEXT, 'Multiple Windows')
    multiwindows.click()
    btn_in_mult_windows = main_page_driver.find_element(By.LINK_TEXT, 'Click Here')
    btn_in_mult_windows.click()
    if len(main_page_driver.window_handles) > 1:
        main_page_driver.switch_to.window(main_page_driver.window_handles[1])
    assert main_page_driver.title in ("New Window")
