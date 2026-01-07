from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
def test_project4():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(chrome_options)
    driver.get("https://www.idrive360.com/enterprise/login")
    time.sleep(5)
    email=driver.find_element(By.ID, "username")
    email.send_keys("augtest_040823@idrive.com")
    time.sleep(5)
    password=driver.find_element(By.ID,"password")
    password.send_keys("123456")
    sign_button=driver.find_element(By.ID, "frm-btn")
    sign_button.click()
    time.sleep(20)
    button_name=driver.find_element(By.CLASS_NAME,"id-tkn-btn")
    print(button_name.text)
    assert "Your free trial has expired\nUpgrade Now!"==button_name.text
    time.sleep(5)
    driver.quit()