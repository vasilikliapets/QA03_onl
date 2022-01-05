from selenium.webdriver.common.by import By
import pytest


def test_complicated_page(browser):
    browser.get('https://ultimateqa.com/complicated-page/')
    button = browser.find_element(
        By.XPATH, '//a[@class="et_pb_button et_pb_button_4 et_pb_bg_layout_light"]')
    button.click()


def test_1_filling_out_form(browser):
    browser.get('https://ultimateqa.com/filling-out-forms/')

    name_field = browser.find_element(
        By.XPATH, '//input[@id="et_pb_contact_name_0"]')
    name_field.send_keys('test name')

    message_field = browser.find_element(
        By.XPATH, '//textarea[@id="et_pb_contact_message_0"]')
    message_field.send_keys('test_message')

    submith_button = browser.find_element(
        By.XPATH, '/html/body/div[1]/div/div/div/article/div/div[1]/div/div/div[2]/div[1]/div/div[2]/form/div/button')
    submith_button.click()


def test_2_filling_form(browser):
    browser.get('https://ultimateqa.com/filling-out-forms/')

    name_field = browser.find_element(
        By.XPATH, '//input[@id="et_pb_contact_name_0"]')
    name_field.send_keys('test name')

    submith_button = browser.find_element(
        By.XPATH, '/html/body/div[1]/div/div/div/article/div/div[1]/div/div/div[2]/div[1]/div/div[2]/form/div/button')
    submith_button.click()

    error_message = browser.find_element(
        By.XPATH, '//div[@class="et-pb-contact-message"]')

    assert 'Make sure you fill in all required fields.' in error_message.text


def test_3_filling_form(browser):
    browser.get('https://ultimateqa.com/filling-out-forms/')

    message_field = browser.find_element(
        By.XPATH, '//textarea[@id="et_pb_contact_message_0"]')
    message_field.send_keys('test_message')

    submith_button = browser.find_element(
        By.XPATH, '/html/body/div[1]/div/div/div/article/div/div[1]/div/div/div[2]/div[1]/div/div[2]/form/div/button')
    submith_button.click()

    error_message = browser.find_element(
        By.XPATH, '//div[@class="et-pb-contact-message"]')

    assert 'Make sure you fill in all required fields.' in error_message.text
