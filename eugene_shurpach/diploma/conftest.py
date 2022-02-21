import mysql.connector as mysql
import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Chrome(executable_path=r"C:\chromedriver\chromedriver.exe")
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def db_connect():
    db = mysql.connect(
        host='localhost',
        user='root',
        database='litecart')
    db_connect = db.cursor()
    yield db_connect
    db.close()
