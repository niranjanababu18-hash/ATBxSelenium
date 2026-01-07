from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
def test_project4():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(chrome_options)
    driver.get("https://app.vwo.com")
    email=driver.find_element(By.ID, "login-username")
    email.send_keys("admin@admin.com")
    time.sleep(5)
    password=driver.find_element(By.ID,"login-password")
    password.send_keys("admin")
    sign_button=driver.find_element(By.ID, "js-login-btn")
    sign_button.click()
    time.sleep(2)
    error=driver.find_element(By.CLASS_NAME,"notification-box-description")
    print(error.text)
    assert "Your email, password, IP address or location did not match"==error.text
    time.sleep(5)
    driver.quit()