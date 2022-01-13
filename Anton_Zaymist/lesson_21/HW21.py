from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


# Для выполнения ДЗ используйте сайт http://the-internet.herokuapp.com/
# Результатом выполненного ДЗ считается наличие необходимых фикстур и тестов!
# Задание 1:


# Перейти по ссылке Form Authentication
def test_login_positive(hw21_ex1_driver):
    hw21_ex1_driver.fullscreen_window()
    # Ввести имя пользователя tomsmith
    username_input = hw21_ex1_driver.find_element(By.XPATH, "//*[@id='username']")
    username_input.send_keys('tomsmith')
    # Ввести пароль SuperSecretPassword!
    password_input = hw21_ex1_driver.find_element(By.XPATH, "//*[@id='password']")
    password_input.send_keys('SuperSecretPassword!')
    login_button = hw21_ex1_driver.find_element(By.XPATH, "//*[@id='login']/button")
    login_button.click()
    # Удостоверится что вы залогинились успешно
    successfully_login = hw21_ex1_driver.find_element(By.XPATH, "//*[@id='flash']").text
    assert successfully_login in 'You logged into a secure area!\n×'


# Сделать все тоже самое, но с другим логином и паролем и удостоверится что логин не прошел
def test_login_negative(hw21_ex1_driver):
    hw21_ex1_driver.fullscreen_window()
    # Ввести имя пользователя tomsmith
    username_input = hw21_ex1_driver.find_element(By.XPATH, "//*[@id='username']")
    username_input.send_keys('tomsmithh')
    # Ввести пароль SuperSecretPassword!
    password_input = hw21_ex1_driver.find_element(By.XPATH, "//*[@id='password']")
    password_input.send_keys('SuperSecretPassword!')
    login_button = hw21_ex1_driver.find_element(By.XPATH, "//*[@id='login']/button")
    login_button.click()
    # Удостоверится что вы залогинились не успешно
    unsuccessfully_login = hw21_ex1_driver.find_element(By.XPATH, "//*[@id='flash']").text
    assert unsuccessfully_login in 'Your username is invalid!\n×'


# Задание 2
def test_checkboxes1(hw21_ex2_driver):
    hw21_ex2_driver.fullscreen_window()
    # На главной странице перейти по ссылке Checkboxes
    open_checkboxes = hw21_ex2_driver.find_element(By.XPATH, "//*[@id='content']/ul/li[6]/a")
    open_checkboxes.click()
    # Установить галочку для второго чекбокса и проверить что она установлена
    set_checkbox2 = hw21_ex2_driver.find_element(By.XPATH, "//*[@id='checkboxes']/input[2]")
    assert set_checkbox2.is_selected()
    # Для первого чекбокса убрать галочку и протестировать, что ее нет
    set_checkbox1 = hw21_ex2_driver.find_element(By.XPATH, "//*[@id='checkboxes']/input[1]")
    assert set_checkbox1.is_selected() is False


# Задание 3
def test_checkboxes2(hw21_ex2_driver):
    hw21_ex2_driver.fullscreen_window()
    # На главной странице перейти по ссылке Multiple Windows
    open_multiple_windows = hw21_ex2_driver.find_element(By.XPATH, "//*[@id='content']/ul/li[33]/a")
    open_multiple_windows.click()
    # После этого найти и нажать на ссылку Click here
    open_link = hw21_ex2_driver.find_element(By.XPATH, "//*[@id='content']/div/a")
    open_link.click()
    # Убедиться, что открылось новое окно и проверить что заголовок страницы – New window
    new_window = hw21_ex2_driver.window_handles[1]
    hw21_ex2_driver.switch_to.window(new_window)
    title = hw21_ex2_driver.title

    assert title == 'New Window'

# Задание 4
def test_add_elements(hw21_ex2_driver):
    hw21_ex2_driver.fullscreen_window()
    # На главной странице перейти по ссылке Add/Remove elements
    open_multiple_windows = hw21_ex2_driver.find_element(By.XPATH, "//*[@id='content']/ul/li[2]/a")
    open_multiple_windows.click()
    # Проверить что при нажатии на кнопку Add element, появляется новый элемент
    add_new_element = hw21_ex2_driver.find_element(By.XPATH, "//*[@id='content']/div/button")
    add_new_element.click()
    assert add_new_element.is_enabled() == True


# Написать отдельный тест, который проверяет удаление элементов
def test_del_elements(hw21_ex2_driver):
    try:
        hw21_ex2_driver.fullscreen_window()
        # На главной странице перейти по ссылке Add/Remove elements
        open_multiple_windows = hw21_ex2_driver.find_element(By.XPATH, "//*[@id='content']/ul/li[2]/a")
        open_multiple_windows.click()
        add_new_element = hw21_ex2_driver.find_element(By.XPATH, "//*[@id='content']/div/button")
        add_new_element.click()
        del_element = hw21_ex2_driver.find_element(By.XPATH, "//*[@id='elements']/button")
        del_element.click()
        new_element_ex = hw21_ex2_driver.find_element(By.XPATH, '//button[@class="added-manually"]')
    except NoSuchElementException:
        new_element_ex = False

    assert new_element_ex == False
