from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
def test_project_positive():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(chrome_options)
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    make_appointment_button=driver.find_element(By.ID, "btn-make-appointment")
    make_appointment_button.click()
    time.sleep(5)
    user_name=driver.find_element(By.NAME,"username")
    user_name.send_keys("John Doe")
    password=driver.find_element(By.NAME,"password")
    password.send_keys("ThisIsNotAPassword")
    login_button=driver.find_element(By.ID, "btn-login")
    login_button.click()
    time.sleep(10)
    driver.quit()