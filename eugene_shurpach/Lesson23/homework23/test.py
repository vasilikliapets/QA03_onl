import pytest
from selenium.webdriver.common.by import By


# Из автотеста не воспринимается заполнение полей
def test_success_login(page_driver):
    name = page_driver.find_element(By.XPATH, "//*[@id='et_pb_contact_name_0']")
    name.send_keys('Username')
    message = page_driver.find_element(By.XPATH, "//*[@id='et_pb_contact_message_0']")
    message.send_keys('Text text text')
    submit_btn = page_driver.find_element(By.XPATH, "//*[@name='et_builder_submit_button'][1]")
    submit_btn.click()
    check_message = page_driver.find_element(By.XPATH, "//*[@class='et-pb-contact-message']")
    assert 'Form filled out successfully' in check_message.text


def test_login_without_message(page_driver):
    name = page_driver.find_element(By.XPATH, "//*[@id='et_pb_contact_name_0']")
    name.send_keys('Username')
    submit_btn = page_driver.find_element(By.XPATH, "//*[@name='et_builder_submit_button'][1]")
    submit_btn.click()
    check_message = page_driver.find_element(By.XPATH, "//*[@class='et-pb-contact-message']")
    assert 'Make sure you fill in all required fields.' in check_message.text


def test_login_without_name(page_driver):
    message = page_driver.find_element(By.XPATH, "//*[@id='et_pb_contact_message_0']")
    message.send_keys('Text text text')
    submit_btn = page_driver.find_element(By.XPATH, "//*[@name='et_builder_submit_button'][1]")
    submit_btn.click()
    check_message = page_driver.find_element(By.XPATH, "//*[@class='et-pb-contact-message']")
    assert 'Make sure you fill in all required fields.' in check_message.text
    