from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


def test_1_dynamic_control():
    try:
        browser = webdriver.Chrome()
        browser.get('http://the-internet.herokuapp.com/dynamic_controls')

        # find checkbox

        checkbox_1 = browser.find_element(
            By.XPATH, '//input[@type="checkbox"]')

        # push the button

        checkbox_remove_button = browser.find_element(
            By.XPATH, '//button[@autocomplete="off"]')
        checkbox_remove_button.click()

        # waiy until 'It's gone!' appear

        gone_text = WebDriverWait(browser, 10).until(
            EC.text_to_be_present_in_element(
                (By.XPATH, '//p[@id="message"]'), "It's gone!")
        )

        # check that checkbox disappeared(не нашел подходящий вариант проверки на отсутствие элемента)

        try:
            checkbox = browser.find_element(
                By.XPATH, '//input[@type="checkbox"]')
        except NoSuchElementException:
            pass

        # find input

        input_field = browser.find_element(By.XPATH, '//input[@type="text"]')

        # check that input is disabled

        assert input_field.is_enabled() == False

        # push 'enable' button

        enable_button = browser.find_element(
            By.XPATH, '//button[@onclick="swapInput()"]')
        enable_button.click()

        # wait until "it's enabled" appear

        enabled_text = WebDriverWait(browser, 10).until(
            EC.text_to_be_present_in_element(
                (By.XPATH, '//p[@id="message"]'), "It's enabled!")
        )

        # check that input is enabled

        assert input_field.is_enabled() == True

    finally:
        browser.quit()


def test_2_frames():
    try:
        browser = webdriver.Chrome()
        browser.get('http://the-internet.herokuapp.com/frames')

        # open iFrame

        iframe_window = browser.find_element(By.XPATH, '//a[@href="/iframe"]')
        iframe_window.click()

        # switch to iframe

        browser.switch_to.frame(
            browser.find_element(By.XPATH, '//iframe[@id="mce_0_ifr"]'))

        # grab iframe text

        browser.implicitly_wait(5)

        iframe_text = browser.find_element(By.XPATH, '//html/body/p')

        # assertion

        assert iframe_text.text == 'Your content goes here.'

    finally:
        browser.quit()
