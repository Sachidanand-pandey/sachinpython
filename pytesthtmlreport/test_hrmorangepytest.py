import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest
class Testhrm():
    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        yield
        self.driver.close()
    def test_homepagetitle(self,setup):
        self.driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
        time.sleep(4)
        assert self.driver.title=="OrangeHRM23"
    def test_login(self,setup):
        self.driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
        time.sleep(4)
        self.driver.find_element(By.XPATH,'//input[@name="username"]').send_keys('Admin')
        self.driver.find_element(By.XPATH,'//input[@name="password"]').send_keys('admin123')
        self.driver.find_element(By.XPATH,'//button[@type="submit"]').click()
        assert self.driver.title=="OrangeHRM"