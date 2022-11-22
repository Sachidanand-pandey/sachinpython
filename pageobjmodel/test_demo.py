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
    @allure.feature('verify the title of the page')
    @allure.story('first test case')
    @allure.description('in this we verify the tittle of the page')
    @allure.step('go to the page and verify the title of the page')
    def test_homepagetitle(self,setup):
        self.driver.get('http://tutorialsninja.com/demo/')
        time.sleep(4)
        actual_tittle = self.driver.title
        if actual_tittle == 'Your Story':
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="verifytittle", attachment_type=AttachmentType.PNG)
            print('test case is fail')
            assert False
    @allure.severity(severity_level='MAJOR')
    @allure.feature('verify the cart price')
    @allure.story('second test case')
    @allure.description('in this we add the product into cart and verify the price')
    @allure.step('go to the page and add the product to the cart and verify the price of the product are same')
    def test_login(self, setup):
        self.driver.get('http://tutorialsninja.com/demo/')
        time.sleep(4)
        s = self.driver.find_element(By.XPATH, '//*[@id="search"]/input')
        s.send_keys('Macbook')
        s.send_keys(Keys.ENTER)
        time.sleep(5)
        self.driver.find_element(By.XPATH, '//*[@id="content"]/div[3]/div/div/div[2]/div[2]/button').click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, '//div[@id="cart"]/button').click()
        a = self.driver.find_element(By.XPATH, '//*[@id="cart"]/ul/li[2]/div/table/tbody/tr[1]/td[2]')
        d = a.text
        e = d.split('$')
        print(e[1])
        b = self.driver.find_element(By.XPATH, '//*[@id="cart"]/ul/li[2]/div/table/tbody/tr[2]/td[2]')
        f = b.text
        g = f.split('$')
        print(g[1])
        c = self.driver.find_element(By.XPATH, '//*[@id="cart"]/ul/li[2]/div/table/tbody/tr[3]/td[2]')
        h = c.text
        i = h.split('$')
        print(i[1])
        result = float(float(e[1])+float(g[1])+float(i[1]))
        print(result)
        v = self.driver.find_element(By.XPATH, '//*[@id="cart"]/ul/li[2]/div/table/tbody/tr[4]/td[2]')
        res = v.text
        ver = res.split('$')
        resu = float(ver[1])
        if result == resu:
            print('test case pass')
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name="verifyprice", attachment_type=AttachmentType.PNG)
        else:
            assert False

    @allure.severity(severity_level='CRITICAL')
    @allure.feature('verify the mackbook')
    @allure.story('third test case')
    @allure.description('in this we add the product into cart and verify the same product in the cart or not')
    @allure.step('go to the page and add the product into the cart and verify the same product in the cart')
    def test_verify(self, setup):
        self.driver.get('http://tutorialsninja.com/demo/')
        time.sleep(2)
        a = self.driver.find_element(By.XPATH, '//nav[@id="menu"]/div[2]/ul/li[2]/a')
        a.click()
        time.sleep(4)
        b = self.driver.find_element(By.XPATH, "//a[text()='Show All Laptops & Notebooks']")
        b.click()
        time.sleep(4)
        c = self.driver.find_element(By.XPATH, '//i[@class="fa fa-th-list"]')
        c.click()
        time.sleep(4)
        d = self.driver.find_element(By.XPATH, '//*[@id="content"]/div[4]/div[3]/div/div[2]/div[2]/button[1]')
        d.click()
        time.sleep(3)
        e = self.driver.find_element(By.XPATH, '//span[@id="cart-total"]')
        e.click()
        f = self.driver.find_element(By.XPATH, '//td[@class="text-left"]/a')
        g = f.text
        print(g)
        if g == 'MacBook Air':
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name="verifcart", attachment_type=AttachmentType.PNG)
        else:
            assert False

    @allure.severity(severity_level='CRITICAL')
    @allure.feature('verify the tablets')
    @allure.story('fourth test case')
    @allure.description('in this we add the product into cart and verify the same product in the cart or not')
    @allure.step('go to the page and add the product into the cart and verify the same product in the cart')
    def test_tablets(self,setup):
        self.driver.get('http://tutorialsninja.com/demo/')
        time.sleep(4)
        a = self.driver.find_element(By.XPATH,"//a[text()='Tablets']")
        a.click()
        time.sleep(4)
        b = self.driver.find_element(By.XPATH,'//*[@id="content"]/div[2]/div/div/div[2]/div[2]/button[1]')
        b.click()
        time.sleep(3)
        c = self.driver.find_element(By.XPATH,'//span[@id="cart-total"]')
        c.click()
        time.sleep(3)
        d = self.driver.find_element(By.XPATH,'//*[@id="cart"]/ul/li[1]/table/tbody/tr/td[2]/a')
        e = d.text
        print(e)
        if e == 'Samsung Galaxy Tab 10.1':
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name='verifytab',attachment_type=AttachmentType.PNG)
        else:
            assert False

    @allure.severity(severity_level='MAJOR')
    @allure.feature('verify the cam')
    @allure.story('fifth test case')
    @allure.description('in this we add the product into cart and verify the same product in the cart or not')
    @allure.step('go to the page and add the product into the cart and verify the same product in the cart')
    def test_phone(self,setup):
        self.driver.get('http://tutorialsninja.com/demo/')
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//a[text()='Phones & PDAs']").click()
        time.sleep(4)
        a=self.driver.find_element(By.XPATH,'//*[@id="content"]/div[2]/div[2]/div/div[2]/div[2]/button[1]')
        a.click()
        time.sleep(4)
        b=self.driver.find_element(By.XPATH,'//*[@id="cart-total"]')
        b.click()
        time.sleep(3)
        c=self.driver.find_element(By.XPATH,'//*[@id="cart"]/ul/li[1]/table/tbody/tr/td[2]/a')
        d=c.text
        print(d)
        if d=='iPhone':
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name='verifycam', attachment_type=AttachmentType.PNG)
        else:
            assert False

    @allure.severity(severity_level='MAJOR')
    @allure.feature('verify the cam')
    @allure.story('fifth test case')
    @allure.description('in this we add the product into cart and verify the same product in the cart or not')
    @allure.step('go to the page and add the product into the cart and verify the same product in the cart')
    def test_camera(self, setup):
        self.driver.get('http://tutorialsninja.com/demo/')
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="menu"]/div[2]/ul/li[7]/a').click()
        time.sleep(4)
        a = self.driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[2]/div/div[2]/div[2]/button[1]')
        a.click()
        time.sleep(4)
        b = self.driver.find_element(By.XPATH, '//*[@id="cart-total"]')
        b.click()
        time.sleep(3)
        c = self.driver.find_element(By.XPATH, '//*[@id="cart"]/ul/li[1]/table/tbody/tr/td[2]/a')
        d = c.text
        print(d)
        if d == 'Nikon D300':
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name='verifycam', attachment_type=AttachmentType.PNG)
        else:
            assert False




