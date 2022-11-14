import time
from selenium import webdriver
from selenium.webdriver.common.by import By
class demo():
    def __init__(self):
        from webdriver_manager.chrome import ChromeDriverManager
        driver= webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get('https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F')
        time.sleep(3)
        a=driver.find_element(By.XPATH,'//input[@id="Email"]')
        a.clear()
        a.send_keys("admin@yourstore.com")
        time.sleep(3)
        b=driver.find_element(By.XPATH,'//input[@id="Password"]')
        b.clear()
        b.send_keys("admin")
        driver.find_element(By.XPATH,'//button[@class="button-1 login-button"]').click()








