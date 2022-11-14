from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
class Homepage():
    url='https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F'
    email='//input[@id="Email"]'
    pasw='//input[@id="Password"]'
    login='//button[@class="button-1 login-button"]'
    def __init__(self,driver):
        self.driver=driver
    def chrome1(self):
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    def visit(self):
        self.driver.get(self.url)
    def username(self):
        a=self.driver.find_element(By.XPATH,self.email)
        a.clear()
        a.send_keys("admin@yourstore.com")
    def password(self):
        b =self.driver.find_element(By.XPATH,self.pasw)
        b.clear()
        b.send_keys("admin")
    def submit(self):
        self.driver.find_element(By.XPATH,self.login).click()
        self.driver.get_screenshot_as_file("screenshotlognpage.png")
    def closed(self):
        self.driver.close()


