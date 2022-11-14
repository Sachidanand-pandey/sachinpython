import time
from selenium import webdriver
from pageobjmodel.parapom import loginlocator
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
class signin():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(loginlocator.url)
    time.sleep(6)
    driver.find_element(*loginlocator.usernam).send_keys(loginlocator.user)
    time.sleep(4)
    driver.find_element(*loginlocator.passwor).send_keys(loginlocator.pwss)
    driver.find_element(*loginlocator.button).click()
    driver.close()
