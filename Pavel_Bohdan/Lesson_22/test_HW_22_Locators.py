from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Поиск всех локаторов


def css_locator():

    try:

        """1. Поиск по CSS локаторам"""

        browser = webdriver.Chrome()
        browser.get('https://www.saucedemo.com/')

        user_name = browser.find_element(By.CSS_SELECTOR, "#user-name")
        user_name.send_keys('standard_user')
        password = browser.find_element(By.CSS_SELECTOR, "#password")
        password.send_keys('secret_sauce')
        login_button = browser.find_element(By.CSS_SELECTOR, "#login-button")
        login_button.click()

        sort_button = browser.find_element(
            By.CSS_SELECTOR, '.product_sort_container').click()
        sort_az = browser.find_element(
            By.CSS_SELECTOR, '.product_sort_container > option:nth-child(1)')
        sort_za = browser.find_element(
            By.CSS_SELECTOR, '.product_sort_container > option:nth-child(2)')
        sort_lohi = browser.find_element(
            By.CSS_SELECTOR, '.product_sort_container > option:nth-child(3)')
        sort_hilo = browser.find_element(
            By.CSS_SELECTOR, '.product_sort_container > option:nth-child(4)')

        shopping_cart = browser.find_element(
            By.CSS_SELECTOR, ".shopping_cart_link")

        backpack = browser.find_element(
            By.CSS_SELECTOR, "#item_4_title_link > div:nth-child(1)").text
        backpack_cart = browser.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack")
        backpack_price = browser.find_element(
            By.CSS_SELECTOR, "div.inventory_item:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1)").text
        backpack_add_to_cart = browser.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack")

        bike_light = browser.find_element(
            By.CSS_SELECTOR, "#item_0_title_link > div:nth-child(1)").text
        bike_light_cart = browser.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bike-light")
        bike_light_price = browser.find_element(
            By.CSS_SELECTOR, "div.inventory_item:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1)").text
        bike_light_add_to_cart = browser.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bike-light")

        bolt_t_shirt = browser.find_element(
            By.CSS_SELECTOR, "#item_1_title_link > div:nth-child(1)").text
        bolt_t_shirt_cart = browser.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt")
        bolt_t_shirt_price = browser.find_element(
            By.CSS_SELECTOR, "div.inventory_item:nth-child(3) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1)").text
        bolt_t_shirt_add_to_cart = browser.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt")

        fleece_jacket = browser.find_element(
            By.CSS_SELECTOR, "#item_5_title_link > div:nth-child(1)").text
        fleece_jacket_cart = browser.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-fleece-jacket")
        fleece_jacket_price = browser.find_element(
            By.CSS_SELECTOR, "div.inventory_item:nth-child(4) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1)").text
        flecee_jacket_add_to_cart = browser.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-fleece-jacket")

        onesie = browser.find_element(
            By.CSS_SELECTOR, "#item_2_title_link > div:nth-child(1)").text
        onesie_cart = browser.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie")
        onesie_price = browser.find_element(
            By.CSS_SELECTOR, "div.inventory_item:nth-child(5) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1)").text
        onisie_add_to_cart = browser.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie")

        test_t_shirt = browser.find_element(
            By.CSS_SELECTOR, "#item_3_title_link > div:nth-child(1)").text
        test_t_shirt_cart = browser.find_element(
            By.CSS_SELECTOR, "#add-to-cart-test\.allthethings\(\)-t-shirt-\(red\)")
        test_t_shirt_price = browser.find_element(
            By.CSS_SELECTOR, "div.inventory_item:nth-child(6) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1)").text
        test_t_shirt_add_to_cart = browser.find_element(
            By.CSS_SELECTOR, "#add-to-cart-test\.allthethings\(\)-t-shirt-\(red\)")

        print(backpack, backpack_price)
        print(bike_light, bike_light_price)
        print(bolt_t_shirt, bolt_t_shirt_price)
        print(fleece_jacket, fleece_jacket_price)
        print(onesie, onesie_price)
        print(test_t_shirt, test_t_shirt_price)

    finally:

        browser.quit()

# Методы для поиска остальных функциональных элементов на странице


def open_menu(browser):
    menu_button = browser.find_element(
        By.CSS_SELECTOR, "#react-burger-menu-btn")
    return menu_button


def twitter_link(browser):
    twitter_link_button = browser.find_element(
        By.XPATH, '//a[@href="https://twitter.com/saucelabs"]')


def facebook_link(browser):
    facebook_link_button = browser.find_element(
        By.XPATH, '//a[@href="https://www.facebook.com/saucelabs"]')


def linkedin_link(browser):
    linkedin_link_button = browser.find_element(
        By.XPATH, '//a[@href="https://www.linkedin.com/company/sauce-labs/"]')


if __name__ == "__main__":
    css_locator()
