from selenium import webdriver
from selenium.webdriver.common.by import By


def test_xpath_locators():
    browser = webdriver.Chrome()
    browser.get('https://www.saucedemo.com/')

    robot_pic = browser.find_element(By.XPATH, "//*[@id='root']/div/div[2]/div[1]/div[2]")
    login_logo = browser.find_element(By.XPATH, "//*[@id='root']/div/div[1]")

    user_name = browser.find_element(By.XPATH, '//*[@id="user-name"]')
    user_name.send_keys('standard_user')
    password = browser.find_element(By.XPATH, '//*[@id="password"]')
    password.send_keys('secret_sauce')
    login = browser.find_element(By.XPATH, '//*[@id="login-button"]')
    login.click()

    labs_backpack = browser.find_element(
        By.XPATH, "//*[@id='item_4_title_link']/div").text
    labs_backpack_cart = browser.find_element(
        By.XPATH, "//*[@id='add-to-cart-sauce-labs-backpack']")
    labs_backpack_price = browser.find_element(
        By.XPATH, "//*[@id='inventory_container']/div/div[1]/div[2]/div[2]/div").text
    print(labs_backpack)
    print(labs_backpack_price)

    sauce_labs_bike_light = browser.find_element(
        By.XPATH, "//*[@id='item_0_title_link']/div").text
    sauce_labs_bike_light_cart = browser.find_element(
        By.XPATH, "//*[@id='add-to-cart-sauce-labs-bike-light']")
    sauce_labs_bike_light_cart_price = browser.find_element(
        By.XPATH, "//*[@id='inventory_container']/div/div[2]/div[2]/div[2]/div").text
    print(sauce_labs_bike_light)
    print(sauce_labs_bike_light_cart_price)

    sauce_labs_bolt_t_shirt = browser.find_element(
        By.XPATH, "//*[@id='item_1_title_link']/div").text
    sauce_labs_bolt_t_shirt_cart = browser.find_element(
        By.XPATH, "//*[@id='add-to-cart-sauce-labs-bolt-t-shirt']")
    sauce_labs_bolt_t_shirt_price = browser.find_element(
        By.XPATH, "//*[@id='inventory_container']/div/div[3]/div[2]/div[2]/div").text
    print(sauce_labs_bolt_t_shirt)
    print(sauce_labs_bolt_t_shirt_price)

    sauce_labs_fleece_jacket = browser.find_element(
        By.XPATH, "//*[@id='item_5_title_link']/div").text
    sauce_labs_fleece_jacket_cart = browser.find_element(
        By.XPATH, "//*[@id='add-to-cart-sauce-labs-fleece-jacket']")
    sauce_labs_fleece_jacket_price = browser.find_element(
        By.XPATH, "//*[@id='inventory_container']/div/div[4]/div[2]/div[2]/div").text
    print(sauce_labs_fleece_jacket)
    print(sauce_labs_fleece_jacket_price)

    sauce_labs_onesie = browser.find_element(
        By.XPATH, "//*[@id='item_2_title_link']/div").text
    sauce_labs_onesie_cart = browser.find_element(
        By.XPATH, "//*[@id='add-to-cart-sauce-labs-onesie']")
    sauce_labs_onesie_price = browser.find_element(
        By.XPATH, "//*[@id='inventory_container']/div/div[5]/div[2]/div[2]/div").text
    print(sauce_labs_onesie)
    print(sauce_labs_onesie_price)

    red_t_shirt = browser.find_element(
        By.XPATH, "//*[@id='item_3_title_link']/div").text
    red_t_shirt_cart = browser.find_element(
        By.XPATH, "//*[@id='add-to-cart-test.allthethings()-t-shirt-(red)']")
    red_t_shirt_price = browser.find_element(
        By.XPATH, "//*[@id='inventory_container']/div/div[6]/div[2]/div[2]/div").text
    print(red_t_shirt)
    print(red_t_shirt_price)


class OtherButtons:

    @staticmethod
    def menu_button(driver):
        menu_button = driver.find_element(By.XPATH, "//*[@id='react-burger-menu-btn']")
        return menu_button

    @staticmethod
    def filter(driver):
        filter_button = driver.find_element(By.XPATH, "//*[@id='header_container']/div[2]/div[2]/span/select")
        return filter_button

    @staticmethod
    def shopping_cart(driver):
        shopping_cart_button = driver.find_element(By.XPATH, "//*[@id='shopping_cart_container']/a")
        return shopping_cart_button

    @staticmethod
    def twitter(driver):
        twitter_link = driver.find_element(By.XPATH, "//*[@id='page_wrapper']/footer/ul/li[1]/a")
        return twitter_link

    @staticmethod
    def facebook(driver):
        facebook_link = driver.find_element(By.XPATH, "//*[@id='page_wrapper']/footer/ul/li[2]/a")
        return
