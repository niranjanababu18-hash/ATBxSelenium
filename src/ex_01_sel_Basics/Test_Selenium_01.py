import pytest
from selenium import webdriver
import allure
@allure.title("Selenium Test")
@allure.description("we will open url and check")
def test_first_selenium():
    driver = webdriver.Chrome()
    driver.get("https://google.com")
    print(driver.title)
    assert driver.title == "Google"