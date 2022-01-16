from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver = Chrome()
driver.get("https://www.saucedemo.com")

# Поиск по CSS
logo = driver.find_element(By.CSS_SELECTOR, '.login_logo')
username = driver.find_element(By.CSS_SELECTOR, '.input_error.form_input[type="text"]')
password = driver.find_element(By.CSS_SELECTOR, '.input_error.form_input[type="password"]')
submit_btn = driver.find_element(By.CSS_SELECTOR, '.submit-button.btn_action')
img_robot = driver.find_element(By.CSS_SELECTOR, '.bot_column')
logins = driver.find_element(By.CSS_SELECTOR, '#login_credentials')
passwords = driver.find_element(By.CSS_SELECTOR, '.login_password')
# Поиск по XPATH
logo_x = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]')
username_x = driver.find_element(By.XPATH, '//*[@id="user-name"]')
password_x = driver.find_element(By.XPATH, '//*[@id="password"]')
submit_btn_x = driver.find_element(By.XPATH, '//*[@id="login-button"]')
img_robot_x = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/div[2]')
logins_x = driver.find_element(By.XPATH, '//*[@id="login_credentials"]')
passwords_x = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div[2]')

# Авторизация
username.send_keys('standard_user')
password.send_keys('secret_sauce')
submit_btn.click()

# Описание товаров
description_of_item_1 = driver.find_element(By.CSS_SELECTOR,
                                            '.inventory_list > :nth-of-type(1) .inventory_item_desc')
description_of_item_2 = driver.find_element(By.CSS_SELECTOR,
                                            '.inventory_list > :nth-of-type(2) .inventory_item_desc')
description_of_item_3 = driver.find_element(By.CSS_SELECTOR,
                                            '.inventory_list > :nth-of-type(3) .inventory_item_desc')
description_of_item_4 = driver.find_element(By.CSS_SELECTOR,
                                            '.inventory_list > :nth-of-type(4) .inventory_item_desc')
description_of_item_5 = driver.find_element(By.CSS_SELECTOR,
                                            '.inventory_list > :nth-of-type(5) .inventory_item_desc')
description_of_item_6 = driver.find_element(By.CSS_SELECTOR,
                                            '.inventory_list > :nth-of-type(6) .inventory_item_desc')

# Кнопка Add to cart
add_to_cart_button_1 = driver.find_element(By.CSS_SELECTOR, '.inventory_list > :nth-of-type(1) button')
add_to_cart_button_2 = driver.find_element(By.CSS_SELECTOR, '.inventory_list > :nth-of-type(2) button')
add_to_cart_button_3 = driver.find_element(By.CSS_SELECTOR, '.inventory_list > :nth-of-type(3) button')
add_to_cart_button_4 = driver.find_element(By.CSS_SELECTOR, '.inventory_list > :nth-of-type(4) button')
add_to_cart_button_5 = driver.find_element(By.CSS_SELECTOR, '.inventory_list > :nth-of-type(5) button')
add_to_cart_button_6 = driver.find_element(By.CSS_SELECTOR, '.inventory_list > :nth-of-type(6) button')

# Листы с названиями и ценами всех товаров
list_name_item = driver.find_elements(By.CSS_SELECTOR, '.inventory_item_name')
list_price_item = driver.find_elements(By.CSS_SELECTOR, '.inventory_item_price')

# Печатаем названия и цены
print(list_name_item[0].text, list_price_item[0].text)
print(list_name_item[1].text, list_price_item[1].text)
print(list_name_item[2].text, list_price_item[2].text)
print(list_name_item[3].text, list_price_item[3].text)
print(list_name_item[4].text, list_price_item[4].text)
print(list_name_item[5].text, list_price_item[5].text)


class Buttons:

    def menu_btn(self):
        menu_btn = driver.find_element(By.CSS_SELECTOR, '#react-burger-menu-btn')
        return menu_btn

    def cart_btn(self):
        cart_btn = driver.find_element(By.CSS_SELECTOR, '.shopping_cart_link')
        return cart_btn

    def filter_btn(self):
        filter_btn = driver.find_element(By.CSS_SELECTOR, '.product_sort_container')
        return filter_btn

    def social_twitter(self):
        social_twitter = driver.find_element(By.CSS_SELECTOR, '.social_twitter[href="https://twitter.com/saucelabs"]')
        return social_twitter

    def social_facebook(self):
        social_facebook = driver.find_element(
            By.CSS_SELECTOR, '.social_facebook[href="https://www.facebook.com/saucelabs"]')
        return social_facebook

    def social_linkedin(self):
        social_linkedin = driver.find_element(
            By.CSS_SELECTOR, '.social_linkedin[href="https://www.linkedin.com/company/sauce-labs/"]')
        return social_linkedin


driver.quit()
