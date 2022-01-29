from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

'''
1.	Откройте страницу: https://ultimateqa.com/complicated-page/
2.	Нажмите на 2-ю сверху кнопку во втором столбце используя:
'''


def complicated_page(browser):
    browser.get('https://ultimateqa.com/complicated-page/')
    button = browser.find_element(
        By.XPATH, '//a[@class="et_pb_button et_pb_button_4 et_pb_bg_layout_light"]')
    button.click()


'''
тест1:
1.	Заполните форму обратной связи
2.	Нажмите на кнопку "Submit"
3.	Проверьте наличие сообщения "Form filled out successfully"
'''


def test_1_filling_out_form(fillingout_forms_page):

    name_field = fillingout_forms_page.find_element(
        By.XPATH, '//input[@id="et_pb_contact_name_0"]')
    name_field.send_keys('test name')

    message_field = fillingout_forms_page.find_element(
        By.XPATH, '//textarea[@id="et_pb_contact_message_0"]')
    message_field.send_keys('test_message')

    submith_button = fillingout_forms_page.find_element(
        By.XPATH, '/html/body/div[1]/div/div/div/article/div/div[1]/div/div/div[2]/div[1]/div/div[2]/form/div/button')
    submith_button.click()

    message = fillingout_forms_page.find_element(
        By.XPATH, '//div[@class="et-pb-contact-message"]').text
    assert 'Make sure you fill in all required fields.' in message


'''
тест2:
1.	Заполните поле "Name"
2.	Нажмите на кнопку "Submit"
3.	Проверьте наличие сообщения об ошибке
'''


def test_2_filling_form(fillingout_forms_page):

    name_field = fillingout_forms_page.find_element(
        By.XPATH, '//input[@id="et_pb_contact_name_0"]')
    name_field.send_keys('test name')

    submith_button = fillingout_forms_page.find_element(
        By.XPATH, '/html/body/div[1]/div/div/div/article/div/div[1]/div/div/div[2]/div[1]/div/div[2]/form/div/button')
    submith_button.click()

    error_message = fillingout_forms_page.find_element(
        By.XPATH, '//div[@class="et-pb-contact-message"]')

    assert 'Make sure you fill in all required fields.' in error_message.text


'''
тест3:
1.	Заполните поле "Message"
2.	Нажмите на кнопку "Submit"
3.	Проверьте наличие сообщения об ошибке
'''


def test_3_filling_form(fillingout_forms_page):

    message_field = fillingout_forms_page.find_element(
        By.XPATH, '//textarea[@id="et_pb_contact_message_0"]')
    message_field.send_keys('test_message')

    submith_button = fillingout_forms_page.find_element(
        By.XPATH, '/html/body/div[1]/div/div/div/article/div/div[1]/div/div/div[2]/div[1]/div/div[2]/form/div/button')
    submith_button.click()

    error_message = fillingout_forms_page.find_element(
        By.XPATH, '//div[@class="et-pb-contact-message"]')

    assert 'Make sure you fill in all required fields.' in error_message.text


if __name__ == "__main__":
    complicated_page(webdriver.Chrome())
