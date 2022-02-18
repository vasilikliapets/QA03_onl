from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
url = "http://localhost/litecart"
driver.get(url)
"""
email = driver.find_element(By.XPATH, '//*[@name="email"]')
email.send_keys('test@test12.com')

password = driver.find_element(By.XPATH, '//*[@name="password"]')
password.send_keys('1235test')

button_login = driver.find_element(By.XPATH, '//button[@name="login"]')
button_login.click()

open_quack1 = driver.find_element(By.XPATH, '//*[@title="Green Duck"]')
open_quack1.click()

click_to_cart = driver.find_element(By.XPATH, '//button[@name="add_cart_product"]')
click_to_cart.click()

button_home = driver.find_element(By.XPATH, '//*[@title="Home"]')
button_home.click()

open_quack1 = driver.find_element(By.XPATH, '//*[@title="Blue Duck"]')
open_quack1.click()

click_to_cart = driver.find_element(By.XPATH, '//button[@name="add_cart_product"]')
click_to_cart.click()

button_home = driver.find_element(By.XPATH, '//*[@title="Home"]')
button_home.click()
"""
"""
count = driver.find_element(By.XPATH, '//*[@name="quantity"]')
count.clear()
count.send_keys('3')

add_quack = driver.find_element(By.XPATH, '//*[@name="add_cart_product"]')
add_quack.click()

open_cart = driver.find_element(By.XPATH, '//*[@id="cart-wrapper"]')
open_cart.click()

order = driver.find_element(By.XPATH, '//*[@name="confirm_order"]')
order.click()
"""