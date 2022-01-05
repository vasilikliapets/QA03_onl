import time

from selenium.webdriver.common.by import By


def test_find_sec_btn(ultinateqa_complic_page):
    """
    Find and Click second button in second colomn
    """
    sec_btn_sec_col = ultinateqa_complic_page.find_element(By.CSS_SELECTOR, "a.et_pb_button_4")
    sec_btn_sec_col.click()


def test1_fill_all_forms_left(ultinateqa_filling_out_forms_page):
    """
    Test: Fill name and message, push "submit", get message:"Thanks for contacting us"
    #But in the task, we should get message "Form filled out successfully"
    """
    name_field = ultinateqa_filling_out_forms_page.find_element(By.XPATH, "//*[@id='et_pb_contact_name_0']")
    mess_field = ultinateqa_filling_out_forms_page.find_element(By.XPATH, "//*[@id='et_pb_contact_message_0']")
    subm_btn = ultinateqa_filling_out_forms_page.find_element(By.XPATH,
                                                              "//*[@id='et_pb_contact_form_0']/div[2]/form/div/button")
    name_field.send_keys("Andry")
    mess_field.send_keys("Hello Everybody!")
    time.sleep(2)
    subm_btn.click()
    text_sucess = ultinateqa_filling_out_forms_page.find_element(By.CSS_SELECTOR,
                                                                 ".et_pb_contact_form_0 > div:nth-child(1) > p:nth-child(1)")
    assert text_sucess.text == "Thanks for contacting us"
    # assert "Form filled out successfully"


def test2_fill_name_form_left(ultinateqa_filling_out_forms_page):
    """
    Test: Fill only name field, push submit, and get error Message
    """
    name_field = ultinateqa_filling_out_forms_page.find_element(By.XPATH, "//*[@id='et_pb_contact_name_0']")
    subm_btn = ultinateqa_filling_out_forms_page.find_element(By.XPATH,
                                                              "//*[@id='et_pb_contact_form_0']/div[2]/form/div/button")
    name_field.send_keys("Andry")
    time.sleep(2)
    subm_btn.click()
    text_error = ultinateqa_filling_out_forms_page.find_element(By.XPATH,
                                                                "//*[@id='et_pb_contact_form_0']/div[1]/ul[1]/li")
    assert text_error.text == "Message"


def test3_fill_message_form_left(ultinateqa_filling_out_forms_page):
    """
    Test: Fill only message field, push submit, and get error Name
    """
    mess_field = ultinateqa_filling_out_forms_page.find_element(By.XPATH, "//*[@id='et_pb_contact_message_0']")
    subm_btn = ultinateqa_filling_out_forms_page.find_element(By.XPATH,
                                                              "//*[@id='et_pb_contact_form_0']/div[2]/form/div/button")
    mess_field.send_keys("My message: Hello Andry, it's Test!")
    time.sleep(2)
    subm_btn.click()
    text_error = ultinateqa_filling_out_forms_page.find_element(By.XPATH,
                                                                "//*[@id='et_pb_contact_form_0']/div[1]/ul[1]/li")

    assert text_error.text == "Name"
