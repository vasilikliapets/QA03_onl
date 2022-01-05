from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def test_css_locator():

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

        bike_light = browser.find_element(
            By.CSS_SELECTOR, "#item_0_title_link > div:nth-child(1)").text
        bike_light_cart = browser.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bike-light")
        bike_light_price = browser.find_element(
            By.CSS_SELECTOR, "div.inventory_item:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1)").text

        bolt_t_shirt = browser.find_element(
            By.CSS_SELECTOR, "#item_1_title_link > div:nth-child(1)").text
        bolt_t_shirt_cart = browser.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt")
        bolt_t_shirt_price = browser.find_element(
            By.CSS_SELECTOR, "div.inventory_item:nth-child(3) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1)").text

        fleece_jacket = browser.find_element(
            By.CSS_SELECTOR, "#item_5_title_link > div:nth-child(1)").text
        fleece_jacket_cart = browser.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-fleece-jacket")
        fleece_jacket_price = browser.find_element(
            By.CSS_SELECTOR, "div.inventory_item:nth-child(4) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1)").text

        onesie = browser.find_element(
            By.CSS_SELECTOR, "#item_2_title_link > div:nth-child(1)").text
        onesie_cart = browser.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie")
        onesie_price = browser.find_element(
            By.CSS_SELECTOR, "div.inventory_item:nth-child(5) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1)").text

        test_t_shirt = browser.find_element(
            By.CSS_SELECTOR, "#item_3_title_link > div:nth-child(1)").text
        test_t_shirt_cart = browser.find_element(
            By.CSS_SELECTOR, "#add-to-cart-test\.allthethings\(\)-t-shirt-\(red\)")
        test_t_shirt_price = browser.find_element(
            By.CSS_SELECTOR, "div.inventory_item:nth-child(6) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1)").text

    finally:

        browser.quit()


def test_xpath_locators():

    try:

        """1. Поиск по XPath локаторам"""

        browser = webdriver.Chrome()
        browser.get('https://www.saucedemo.com/')

        user_name = browser.find_element(By.XPATH, '//*[@id="user-name"]')
        user_name.send_keys('standard_user')
        password = browser.find_element(By.XPATH, '//*[@id="password"]')
        password.send_keys('secret_sauce')
        login_button = browser.find_element(
            By.XPATH, '//*[@id="login-button"]')
        login_button.click()

        sort_button = browser.find_element(
            By.XPATH, '//select[@class="product_sort_container"]').click()
        sort_az = browser.find_element(By.XPATH, '//option[@value="az"]')
        sort_za = browser.find_element(By.XPATH, '//option[@value="za"]')
        sort_lohi = browser.find_element(By.XPATH, '//option[@value="lohi"]')
        sort_hilo = browser.find_element(By.XPATH, '//option[@value="hilo"]')

        shopping_cart = browser.find_element(
            By.XPATH, '//*[@class="shopping_cart_link"]')

        backpack = browser.find_element(
            By.XPATH, '//*[@class="inventory_item_name"]').text
        backpack_cart = browser.find_element(
            By.XPATH, '//button[@id="add-to-cart-sauce-labs-backpack"]')
        backpack_price = browser.find_element(
            By.XPATH, '//*[@class="inventory_item_price"]').text

        bike_light = browser.find_element(
            By.XPATH, '//*[@class="inventory_item_name"]').text
        bike_light_cart = browser.find_element(
            By.XPATH, '//button[@id="add-to-cart-sauce-labs-bike-light"]')
        bike_light_price = browser.find_element(
            By.XPATH, '//*[@class="inventory_item_price"]')

        bolt_t_shirt = browser.find_element(
            By.XPATH, '//*[@class="inventory_item_name"]').text
        bolt_t_shirt_cart = browser.find_element(
            By.XPATH, '//button[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')
        bolt_t_shirt_price = browser.find_element(
            By.XPATH, '//*[@class="inventory_item_price"]').text

        fleece_jacket = browser.find_element(
            By.XPATH, '//*[@class="inventory_item_name"]').text
        fleece_jacket_cart = browser.find_element(
            By.XPATH, '//button[@id="add-to-cart-sauce-labs-fleece-jacket"]')
        fleece_jacket_price = browser.find_element(
            By.XPATH, '//*[@id="add-to-cart-sauce-labs-fleece-jacket"]').text

        onesie = browser.find_element(
            By.XPATH, '//*[@class="inventory_item_name"]').text
        onesie_cart = browser.find_element(
            By.XPATH, '//button[@id="add-to-cart-sauce-labs-onesie"]')
        onesie_price = browser.find_element(
            By.XPATH, '//*[@class="inventory_item_price"]').text

        test_t_shirt = browser.find_element(
            By.XPATH, '//*[@class="inventory_item_name"]').text
        test_t_shirt_cart = browser.find_element(
            By.XPATH, '//button[@id="add-to-cart-test.allthethings()-t-shirt-(red)"]')
        test_t_shirt_price = browser.find_element(
            By.XPATH, '//*[@class="inventory_item_price"]').text

    finally:

        browser.quit()
