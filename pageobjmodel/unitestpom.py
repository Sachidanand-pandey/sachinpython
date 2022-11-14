import unittest
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
url = 'https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F'
email = '//input[@id="Email"]'
pasw = '//input[@id="Password"]'
login = '//button[@class="button-1 login-button"]'
class TestStringMethods(unittest.TestCase):
    def __init__(self, driver):
        self.driver = driver
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        self.driver.get('https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F')
        a = self.driver.find_element(By.XPATH, self.email)
        a.clear()
        a.send_keys("admin@yourstore.com")
        b = self.driver.find_element(By.XPATH, self.pasw)
        b.clear()
        b.send_keys("admin")
        self.driver.find_element(By.XPATH, self.login).click()
    if __name__ == '__main__':
        unittest.main()