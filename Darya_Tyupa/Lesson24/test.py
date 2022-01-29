import time

from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def test_checkbox(controls_page):
    checkbox = controls_page.find_element(By.XPATH, "//input[@type='checkbox']")
    remove_button = controls_page.find_element(By.XPATH, "//*[@id='checkbox-example']//button")
    remove_button.click()
    message = WebDriverWait(controls_page, 10).until(
        EC.text_to_be_present_in_element((By.XPATH, "//p[@id='message']"), 'It\'s gone!'))
    checkbox = controls_page.find_elements(By.XPATH, "//input[@type='checkbox']")
    assert checkbox == []


def test_input(controls_page):
    input_field = controls_page.find_element(By.XPATH, "//input[@type='text']")
    assert input_field.is_enabled() is False
    enable_button = controls_page.find_element(By.XPATH, "//*[@id='input-example']//button")
    enable_button.click()
    message = WebDriverWait(controls_page, 10).until(
             EC.text_to_be_present_in_element((By.XPATH, "//p[@id='message']"), 'It\'s enabled!'))
    assert input_field.is_enabled()


def test_frame(frames_page):
    frames_link = frames_page.find_element(By.XPATH, "//a[@href='/iframe']")
    frames_link.click()
    frames_page.switch_to.frame(frames_page.find_element(By.XPATH, "//iframe"))
    element = frames_page.find_element(By.XPATH, "//p")
    assert element.text == 'Your content goes here.'

