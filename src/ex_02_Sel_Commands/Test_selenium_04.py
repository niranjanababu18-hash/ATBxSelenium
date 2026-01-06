import pytest
from selenium import webdriver
import allure
@allure.title("print the page source")
def test_selenium_commands():
    driver = webdriver.Edge()
    driver.get("https://google.com")
    driver.maximize_window()
    print(driver.page_source)

