import time
from selenium import webdriver
from pom.loginpage import LoginPage
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
class loginpo():
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.get(LoginPage.login)
    driver.maximize_window()
    a = driver.find_element(By.XPATH, LoginPage.textbox_username)
    a.clear()
    a.send_keys("admin@yourstore.com")
    b = driver.find_element(By.XPATH, LoginPage.textbox_password)
    b.clear()
    b.send_keys("admin")
    c = driver.find_element(By.XPATH, LoginPage.button_login)
    c.click()
    time.sleep(3)
