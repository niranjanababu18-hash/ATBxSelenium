import pytest
from selenium import webdriver
import allure
@allure.title("mini project")
@allure.description("we will open url and perform actions")
def test_mini_project():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    driver.maximize_window()
    page_source_html=driver.page_source
    print(driver.title)
    print(driver.current_url)
    assert 'CURA Healthcare Service' in page_source_html
    driver.quit()
