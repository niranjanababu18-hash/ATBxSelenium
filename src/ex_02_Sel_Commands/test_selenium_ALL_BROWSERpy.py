import time
import pytest
from selenium import webdriver
import allure
from selenium.webdriver.chrome.options import Options
#running pararelly-pytest-xdist(module)
def test_chrome_current_url_verification():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/"
    time.sleep(10)
    driver.quit()
def test_edge_current_url_verification():
    driver = webdriver.Edge()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/"
    time.sleep(10)
    driver.quit()
