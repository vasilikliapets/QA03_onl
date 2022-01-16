from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By

driver = Firefox()
driver.get('https://www.saucedemo.com/')

# находим все локаторы для окна логин

login_logo = driver.find_element(By.CSS_SELECTOR, '.login_logo')
bot_picture = driver.find_element(By.CSS_SELECTOR, '.bot_column')
username_field = driver.find_element(By.CSS_SELECTOR, '#user-name')
password_field = driver.find_element(By.CSS_SELECTOR, '#password')
login_button = driver.find_element(By.CSS_SELECTOR, '#login-button')
login_credentials = driver.find_element(By.CSS_SELECTOR, '#login_credentials')
login_password = driver.find_element(By.CSS_SELECTOR, '.login_password')
login_credentials_title = driver.find_element(By.CSS_SELECTOR, '#login_credentials h4')
login_password_title = driver.find_element(By.CSS_SELECTOR, '.login_password h4')

# логинимся
username_field.send_keys('standard_user')
password_field.send_keys('secret_sauce')
login_button.click()

# находим тайтлы для каждого товара
item_name_1 = driver.find_element(By.CSS_SELECTOR, '#item_4_title_link')
item_name_2 = driver.find_element(By.CSS_SELECTOR, '#item_0_title_link')
item_name_3 = driver.find_element(By.CSS_SELECTOR, '#item_1_title_link')
item_name_4 = driver.find_element(By.CSS_SELECTOR, '#item_5_title_link')
item_name_5 = driver.find_element(By.CSS_SELECTOR, '#item_2_title_link')
item_name_6 = driver.find_element(By.CSS_SELECTOR, '#item_3_title_link')

# находим цену для каждого товара
price_1 = driver.find_element(By.CSS_SELECTOR, '.inventory_list > :nth-of-type(1) .inventory_item_price')
price_2 = driver.find_element(By.CSS_SELECTOR, '.inventory_list > :nth-of-type(2) .inventory_item_price')
price_3 = driver.find_element(By.CSS_SELECTOR, '.inventory_list > :nth-of-type(3) .inventory_item_price')
price_4 = driver.find_element(By.CSS_SELECTOR, '.inventory_list > :nth-of-type(4) .inventory_item_price')
price_5 = driver.find_element(By.CSS_SELECTOR, '.inventory_list > :nth-of-type(5) .inventory_item_price')
price_6 = driver.find_element(By.CSS_SELECTOR, '.inventory_list > :nth-of-type(6) .inventory_item_price')

# находим описание для каждого товара
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

# находим кнопку добавить в корзину для каждого товара
add_to_cart_button_1 = driver.find_element(By.CSS_SELECTOR, '.inventory_list > :nth-of-type(1) button')
add_to_cart_button_2 = driver.find_element(By.CSS_SELECTOR, '.inventory_list > :nth-of-type(2) button')
add_to_cart_button_3 = driver.find_element(By.CSS_SELECTOR, '.inventory_list > :nth-of-type(3) button')
add_to_cart_button_4 = driver.find_element(By.CSS_SELECTOR, '.inventory_list > :nth-of-type(4) button')
add_to_cart_button_5 = driver.find_element(By.CSS_SELECTOR, '.inventory_list > :nth-of-type(5) button')
add_to_cart_button_6 = driver.find_element(By.CSS_SELECTOR, '.inventory_list > :nth-of-type(6) button')

# выводим информацию по каждому товару (название и цена)
print(item_name_1.text, price_1.text)
print(item_name_2.text, price_2.text)
print(item_name_3.text, price_3.text)
print(item_name_4.text, price_4.text)
print(item_name_5.text, price_5.text)
print(item_name_6.text, price_6.text)


# по заданию для всех остальных функциональных элементов создаём методы которые их находят и возвращают
class FunctionalButtons:

    @staticmethod
    def find_menu_button():
        menu_button = driver.find_element(By.CSS_SELECTOR, '#react-burger-menu-btn')
        return menu_button

    @staticmethod
    def find_filter():
        filter_button = driver.find_element(By.CSS_SELECTOR, '.product_sort_container')
        return filter_button

    @staticmethod
    def find_shopping_cart():
        shopping_cart_button = driver.find_element(By.CSS_SELECTOR, '.shopping_cart_link')
        return shopping_cart_button

    @staticmethod
    def find_twitter():
        twitter_link = driver.find_element(By.CSS_SELECTOR, 'a[href="https://twitter.com/saucelabs"]')
        return twitter_link

    @staticmethod
    def find_facebook():
        facebook_link = driver.find_element(By.CSS_SELECTOR, 'a[href="https://www.facebook.com/saucelabs"]')
        return facebook_link

    @staticmethod
    def find_linkedin():
        linkedin_link = driver.find_element(By.CSS_SELECTOR, 'a[href="https://www.linkedin.com/company/sauce-labs/"]')
        return linkedin_link
