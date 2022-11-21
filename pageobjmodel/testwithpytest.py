import time
from allure_commons.types import AttachmentType
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import pytest
class Testdemo():
    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        yield
        self.driver.close()

    def test_title(self, setup):
        self.driver.get('https://magento.softwaretestingboard.com/')
        time.sleep(4)
        actual_tittle = self.driver.title
        if actual_tittle == 'LUMA':
            assert True
        else:
            assert False


