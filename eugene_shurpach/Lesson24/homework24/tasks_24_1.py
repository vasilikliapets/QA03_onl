from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = Chrome()
driver.get("http://the-internet.herokuapp.com/dynamic_controls")

# Найти чекбокс
btn_checkbox = driver.find_element(By.XPATH, "//*[@id='checkbox']/input")
btn_remove = driver.find_element(By.XPATH, "//*[@id='checkbox-example']/button")
# Нажать на кнопку
btn_checkbox.click()
btn_remove.click()
# Дождаться надписи “It’s gone”
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'message'))
)
message = driver.find_element(By.ID, 'message')
assert message.text in ('It\'s gone!')
# Проверить, что чекбокса нет
check_checkbox = driver.find_elements(By.XPATH, "//*[@id='checkbox']/input")
assert check_checkbox == []
# Найти инпут
input_field = driver.find_element(By.XPATH, '//*[@id="input-example"]/input')
# Проверить, что он disabled
check_disabled = WebDriverWait(driver, 0).until_not(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="input-example"]/input'))
)
assert check_disabled is False
# Нажать на кнопку
driver.find_element(By.XPATH, '//*[@id="input-example"]/button').click()
# Дождаться надписи “It's enabled!”
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'message'))
)
message = driver.find_element(By.ID, 'message')
assert message.text in ('It\'s enabled!')
# Проверить, что инпут enabled
assert input_field.is_enabled
driver.quit()
