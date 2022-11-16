import time
from allure_commons.types import AttachmentType
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import pytest
class Testhrm():
    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        yield
        self.driver.close()

    @allure.severity(severity_level='MINOR')
    def test_homepagetitle(self,setup):
        self.driver.get('http://tutorialsninja.com/demo/')
        time.sleep(4)
        actual_tittle=self.driver.title
        if actual_tittle == 'Your Store':
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="verifytittle", attachment_type=AttachmentType.PNG)
            print('test case is fail')
            assert False
    @allure.severity(severity_level='MAJOR')
    def test_login(self,setup):
        self.driver.get('http://tutorialsninja.com/demo/')
        time.sleep(4)
        s=self.driver.find_element(By.XPATH,'//*[@id="search"]/input')
        s.send_keys('Macbook')
        s.send_keys(Keys.ENTER)
        time.sleep(5)
        self.driver.find_element(By.XPATH,'//*[@id="content"]/div[3]/div/div/div[2]/div[2]/button').click()
        time.sleep(5)
        self.driver.find_element(By.XPATH,'//div[@id="cart"]/button').click()
        a=self.driver.find_element(By.XPATH,'//*[@id="cart"]/ul/li[2]/div/table/tbody/tr[1]/td[2]')
        d=(a.text)
        e=d.split('$')
        print(e[1])
        b=self.driver.find_element(By.XPATH,'//*[@id="cart"]/ul/li[2]/div/table/tbody/tr[2]/td[2]')
        f=(b.text)
        g=f.split('$')
        print(g[1])
        c=self.driver.find_element(By.XPATH,'//*[@id="cart"]/ul/li[2]/div/table/tbody/tr[3]/td[2]')
        h=(c.text)
        i=h.split('$')
        print(i[1])
        result=float(float(e[1])+float(g[1])+float(i[1]))
        print(result)
        v=self.driver.find_element(By.XPATH,'//*[@id="cart"]/ul/li[2]/div/table/tbody/tr[4]/td[2]')
        res=(v.text)
        ver=res.split('$')
        resu=float(ver[1])
        if result==resu:
            print('test case pass')
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name="verifyprice", attachment_type=AttachmentType.PNG)
        else:
            assert False

    @allure.severity(severity_level='CRITICAL')
    def test_verify(self, setup):
        self.driver.get('http://tutorialsninja.com/demo/')
        time.sleep(2)
        a=self.driver.find_element(By.XPATH,'//nav[@id="menu"]/div[2]/ul/li[2]/a')
        a.click()
        time.sleep(4)
        b=self.driver.find_element(By.XPATH,"//a[text()='Show All Laptops & Notebooks']")
        b.click()
        time.sleep(4)
        c=self.driver.find_element(By.XPATH,'//i[@class="fa fa-th-list"]')
        c.click()
        time.sleep(4)
        d=self.driver.find_element(By.XPATH,'//*[@id="content"]/div[4]/div[3]/div/div[2]/div[2]/button[1]')
        d.click()
        time.sleep(3)

