import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from pageobjmodel.LT_Locator import LT_Locator
username = "student"
password = "Password123"
class LT_Login(unittest.TestCase):
    def __init__(self, driver):
        self.driver = driver
    def chrome1(self):
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    def visit(self):
        self.driver.get("https://practicetestautomation.com/practice-test-login/")
    def get_LT_username(self):
        self.driver.find_element(By.XPATH, LT_Locator.lt_login_user_name)
    def get_LT_password(self):
        self.driver.find_element(By.XPATH, LT_Locator.lt_login_password)

    def get_LT_login_button(self):
        self.driver.find_element(By.XPATH, LT_Locator.lt_login_button)

    if __name__ == '__main__':
        unittest.main()