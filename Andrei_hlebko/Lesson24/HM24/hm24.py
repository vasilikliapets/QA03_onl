from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def test_checkbox(heroku_checkbox_dynamic):
    """
    The Test check checkboxes on this url http://the-internet.herokuapp.com/dynamic_controls
    """
    # a_checkbox = heroku_checkbox_dynamic.find_element(By.CSS_SELECTOR, "#checkbox > input:nth-child(1)")#Вариант 1 черех CSS

    a_checkbox = heroku_checkbox_dynamic.find_element(By.XPATH, "//*[@id='checkbox']/input")
    remove_add_btn = heroku_checkbox_dynamic.find_element(By.XPATH, "//*[@id='checkbox-example']/button")
    remove_add_btn.click()
    msg_its_gone = WebDriverWait(heroku_checkbox_dynamic, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "p#message")))  # Получаем сообщение
    assert msg_its_gone.text == "It\'s gone!", "We didn't remove button"  # Проверяем текст с полученным
    a_checkboxes = heroku_checkbox_dynamic.find_elements(By.XPATH, "//*[@id='checkbox']/input")
    # ^^^ Тут проверяем есть ли чекбоксы, если их нету то получаем пустой список
    assert a_checkboxes == [], "We have some buttons"


def test_input(heroku_checkbox_dynamic):
    """
    The Test check input field on this url http://the-internet.herokuapp.com/dynamic_controls
    """
    field_input = heroku_checkbox_dynamic.find_element(By.XPATH, "//*[@id='input-example']/input")
    assert field_input.is_enabled() is False
    enable_btn = heroku_checkbox_dynamic.find_element(By.XPATH, "//*[@id='input-example']/button")
    enable_btn.click()
    msg_its_enabled = WebDriverWait(heroku_checkbox_dynamic, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "p#message")))  # тут дожидаемся полученный текст
    assert msg_its_enabled.text == "It\'s enabled!" and field_input.is_enabled(), "We have wrong text!"  # Так можно? или два подряд asserta?
    # ^^тут проверяем полученный текст такой ли как в задании, и доступное ли поле для ввода
    # assert field_input.is_enabled()


def test_frame(heroku_frames_page):
    """
    The Test check text on a frame on this url http://the-internet.herokuapp.com/frames
    """
    iframe_link = heroku_frames_page.find_element(By.XPATH, "//*[@href='/iframe']")
    iframe_link.click()
    # driver.switch_to_frame(driver.find_element_by_tag_name("iframe")) - в материале TMS указано делать так, но не работает!
    heroku_frames_page.switch_to.frame(heroku_frames_page.find_element(By.TAG_NAME, "iframe"))
    text_in_paragr = heroku_frames_page.find_element(By.XPATH, "//*[@id='tinymce']/p")
    assert "Your content goes here" in text_in_paragr.text, "We have another text in the frame"
