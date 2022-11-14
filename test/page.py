import time
from selenium import webdriver
from pageobjmodel.LoginPageLocator import LoginpageLocators
from webdriver_manager.chrome import ChromeDriverManager
username='student'
passw='Password123'
class Loginpage():
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.get(LoginpageLocators.url)
    driver.find_element(*LoginpageLocators.EMAIL).send_keys(username)
    driver.find_element(*LoginpageLocators.PASSWORD).send_keys(passw)
    driver.find_element(*LoginpageLocators.SIGNIN).click()
    time.sleep(3)
    driver.close()

