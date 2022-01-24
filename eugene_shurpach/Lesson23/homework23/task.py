from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver = Chrome()
driver.get("https://ultimateqa.com/complicated-page/")

btn_1 = driver.find_element(By.XPATH, "//*[@id='post-579']/div/div[1]/div/div/div[3]/div[2]/div[2]/a")
btn_1.click()
driver.refresh()
btn_2 = driver.find_element(By.CSS_SELECTOR, ".et_pb_button.et_pb_button_4.et_pb_bg_layout_light")
btn_2.click()
driver.refresh()
btn_3 = driver.find_element(By.CLASS_NAME, "et_pb_button_4")
btn_3.click()
driver.quit()

