from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import allure
import pytest
class Testhrm:
    @allure.severity(severity_level='MINOR')
    def test_logo(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
        time.sleep(3)
        sts=self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[1]/img').is_displayed()
        time.sleep(3)
        if sts==True:
            assert false
        else:
            assert True
        self.driver.close()
    @allure.severity(severity_level='NORMAL')
    def test_listemp(self):
        pytest.skip('skipping the test..later i will implement')
    @allure.severity(severity_level='CRITICAL')
    def test_login(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
        time.sleep(4)
        self.driver.find_element(By.XPATH, '//input[@name="username"]').send_keys('Admin')
        self.driver.find_element(By.XPATH, '//input[@name="password"]').send_keys('admin123')
        self.driver.find_element(By.XPATH, '//button[@type="submit"]').click()
        actual_tittle=self.driver.title
        if actual_tittle == 'OrangeHRM123':
            self.driver.close()
            assert True
        else:
            time.sleep(4)
            allure.attach(self.driver.get_screenshot_as_png(),name="testloginScreen",attachment_type=AttachmentType.PNG)
            self.driver.close()
            assert False
