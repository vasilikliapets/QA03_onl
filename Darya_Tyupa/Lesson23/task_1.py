from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By

driver = Firefox()
driver.get('https://ultimateqa.com/complicated-page/')
find_button_by_xpath = driver.find_element(By.XPATH, "//a[contains(@class, 'et_pb_button_4')]")
find_button_by_css = driver.find_element(By.CSS_SELECTOR, "a[class *= 'et_pb_button_4']")

find_button_by_xpath.click()
