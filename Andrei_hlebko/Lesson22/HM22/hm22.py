from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver = Chrome()
driver.get("https://www.saucedemo.com/")

logo = driver.find_element(By.CSS_SELECTOR, '.login_logo')
robot_logo = driver.find_element(By.CSS_SELECTOR, '.bot_column')
username_input = driver.find_element(By.CSS_SELECTOR, '#user-name')

password_input = driver.find_element(By.CSS_SELECTOR, '#password')
btn_login = driver.find_element(By.CSS_SELECTOR, '#login-button')

# ('standard_user')
# ('secret_sauce')
username_input.send_keys('standard_user')
password_input.send_keys('secret_sauce')
btn_login.click()

bag_name_1 = driver.find_element(By.CSS_SELECTOR, 'a#item_4_title_link')
labs_bike_name_2 = driver.find_element(By.CSS_SELECTOR, 'a#item_0_title_link div')
tshirt_name_3 = driver.find_element(By.CSS_SELECTOR, 'a#item_1_title_link div')
fleece_jacket_name_4 = driver.find_element(By.CSS_SELECTOR, 'a#item_5_title_link div')
labs_onesie_5 = driver.find_element(By.CSS_SELECTOR, 'a#item_2_title_link div')
test_all_tshirt_6 = driver.find_element(By.CSS_SELECTOR, 'a#item_3_title_link div')

# inventory_item_price
item1_price = driver.find_element(By.CSS_SELECTOR, 'div.inventory_item:nth-child(1) > div:nth-child(2) > '
                                                   'div:nth-child(2) > div:nth-child(1)')
item2_price = driver.find_element(By.CSS_SELECTOR, 'div.inventory_item:nth-child(2) > div:nth-child(2) >'
                                                   ' div:nth-child(2) > div:nth-child(1)')

item3_price = driver.find_element(By.CSS_SELECTOR, 'div.inventory_item:nth-child(3) > div:nth-child(2) >'
                                                   ' div:nth-child(2) > div:nth-child(1)')
item4_price = driver.find_element(By.CSS_SELECTOR, 'div.inventory_item:nth-child(4) > div:nth-child(2) > '
                                                   'div:nth-child(2) > div:nth-child(1)')
item5_price = driver.find_element(By.CSS_SELECTOR, 'div.inventory_item:nth-child(5) > div:nth-child(2) > '
                                                   'div:nth-child(2) > div:nth-child(1)')
item6_price = driver.find_element(By.CSS_SELECTOR, 'div.inventory_item:nth-child(6) > div:nth-child(2) > '
                                                   'div:nth-child(2) > div:nth-child(1)')

print(bag_name_1.text, item1_price.text)
print(labs_bike_name_2.text, item2_price.text)
print(tshirt_name_3.text, item3_price.text)
print(fleece_jacket_name_4.text, item4_price.text)
print(labs_onesie_5.text, item5_price.text)
print(test_all_tshirt_6.text, item5_price.text)


class FuncBtn:

    @staticmethod
    def find_menu_btn():
        menu_btn = driver.find_element(By.CSS_SELECTOR, '#react-burger-menu-btn')
        return menu_btn

    @staticmethod
    def find_filter():
        filter_btn = driver.find_element(By.CSS_SELECTOR, '.product_sort_container')
        return filter_btn

    @staticmethod
    def find_shopping_cart():
        shopping_cart_btn = driver.find_element(By.CSS_SELECTOR, '.shopping_cart_link')
        return shopping_cart_btn

    @staticmethod
    def find_twitter_link():
        twitter_link = driver.find_element(By.CSS_SELECTOR, 'a[href="https://twitter.com/saucelabs"]')
        return twitter_link

    @staticmethod
    def find_facebook_link():
        facebook_link = driver.find_element(By.CSS_SELECTOR, 'a[href="https://www.facebook.com/saucelabs"]')
        return facebook_link

    @staticmethod
    def find_linkedin_link():
        linkedin_link = driver.find_element(By.CSS_SELECTOR, 'a[href="https://www.linkedin.com/company/sauce-labs/"]')
        return linkedin_link
