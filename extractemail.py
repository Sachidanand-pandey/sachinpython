import time
from allure_commons.types import AttachmentType
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import pytest
class Testemail():
    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        yield
        self.driver.close()
    def test_search(self,setup):
        self.driver.get('https://www.google.com/')
        a=self.driver.find_element(By.XPATH,'//input[@class="gLFyf"]')
        a.send_keys('www.gmail.com')
        a.send_keys(Keys.ENTER)
        self.driver.find_element(By.XPATH,"//h3[text()='Google Accounts: Sign in']").click()
        b=self.driver.find_element(By.XPATH,'//input[@id="identifierId"]')
        b.send_keys('sachinbst41@gmail.com')
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//span[text()='Next']").click()
        time.sleep(3)
        c=self.driver.find_element(By.XPATH,'//input[@type="password"]')
        c.send_keys('utkarsh@123')
        c.send_keys(Keys.ENTER)
        time.sleep(4)



        time.sleep(3)

