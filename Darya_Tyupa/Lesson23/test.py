import time

from selenium.webdriver.common.by import By


#  в этих тестах я вынуждена была использовать тайм слип, имплиситли вэйт тут никак не помогает
def test_successful_submitting(forms_page):
    """This test checks successful filling of form"""
    name_field = forms_page.find_element(By.XPATH, "//*[@id='et_pb_contact_name_0']")
    message_field = forms_page.find_element(By.XPATH, "//*[@id='et_pb_contact_message_0']")
    submit_button = forms_page.find_element(
        By.XPATH, "//*[contains(@class, 'et_pb_column_1 ')]//*[contains(@class,  'et_pb_button')]")
    name_field.send_keys('Darya')
    message_field.send_keys('Hello, friend!')
    time.sleep(3)
    submit_button.click()
    time.sleep(3)
    find_aller_message = forms_page.find_element(By.XPATH, "//*[contains(@class, 'et_pb_column_1 ')]//p")
    assert find_aller_message.text == 'Thanks for contacting us'


def test_message_1(forms_page):
    """This test checks the filling not all required fields(only user name)"""
    name_field = forms_page.find_element(By.XPATH, "//*[@id='et_pb_contact_name_0']")
    submit_button = forms_page.find_element(
        By.XPATH, "//*[contains(@class, 'et_pb_column_1 ')]//*[contains(@class,  'et_pb_button')]")
    name_field.send_keys('Darya')
    time.sleep(3)
    submit_button.click()
    time.sleep(3)
    find_aller_message = forms_page.find_element(By.XPATH, "//*[@class='et-pb-contact-message']//p")
    missing_field = forms_page.find_element(By.XPATH, "//*[@class='et-pb-contact-message']//li")
    assert find_aller_message.text == 'Please, fill in the following fields:'
    assert missing_field.text == 'Message'


def test_message_2(forms_page):
    """This test checks the filling not all required fields(only message field)"""
    message_field = forms_page.find_element(By.XPATH, "//*[@id='et_pb_contact_message_0']")
    submit_button = forms_page.find_element(
        By.XPATH, "//*[contains(@class, 'et_pb_column_1 ')]//*[contains(@class,  'et_pb_button')]")
    message_field.send_keys('Hello, friend!')
    time.sleep(3)
    submit_button.click()
    time.sleep(3)
    find_aller_message = forms_page.find_element(By.XPATH, "//*[@class='et-pb-contact-message']//p")
    missing_field = forms_page.find_element(By.XPATH, "//*[@class='et-pb-contact-message']//li")
    assert find_aller_message.text == 'Please, fill in the following fields:'
    assert missing_field.text == 'Name'
