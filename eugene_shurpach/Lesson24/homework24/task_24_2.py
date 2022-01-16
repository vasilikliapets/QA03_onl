from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = Chrome()
driver.get("http://the-internet.herokuapp.com/frames")

# Открыть iFrame
frame_1 = driver.find_element(By.XPATH, '//*[@id="content"]/div/ul/li[2]/a')
frame_1.click()
# Проверить, что текст внутри параграфа равен “Your content goes here.”
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, 'content'))
)
driver.switch_to.frame(driver.find_element(By.ID, 'mce_0_ifr'))
field = driver.find_element(By.ID, 'tinymce')
assert field.text == ('Your content goes here.')
driver.quit()
