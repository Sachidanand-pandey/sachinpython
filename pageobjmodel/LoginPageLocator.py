from selenium.webdriver.common.by import By
class LoginpageLocators(object):
    url="https://practicetestautomation.com/practice-test-login/"
    EMAIL= (By.XPATH, '//input[@id="username"]')
    PASSWORD= (By.XPATH,'//input[@id="password"]')
    SIGNIN = (By.XPATH, '//button[@id="submit"]')