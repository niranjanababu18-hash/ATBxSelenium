from selenium import webdriver
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions
import time
from selenium.webdriver.common.by import By
def test_project_positive():
    chrome_options = ChromeOptions()
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

def test_project_negative():
    edge_options = EdgeOptions()
    edge_options.add_argument("--start-maximized")
    driver = webdriver.Edge(edge_options)
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    make_appointment_button=driver.find_element(By.ID, "btn-make-appointment")
    make_appointment_button.click()
    time.sleep(5)
    user_name=driver.find_element(By.NAME,"username")
    user_name.send_keys("Niranjana")
    password=driver.find_element(By.NAME,"password")
    password.send_keys("wrongPassword")
    login_button=driver.find_element(By.ID, "btn-login")
    login_button.click()
    time.sleep(2)
    error=driver.find_element(By.CLASS_NAME,"text-danger")
    print(error.text)
    assert "Login failed! Please ensure the username and password are valid."==error.text
    time.sleep(5)
    driver.quit()