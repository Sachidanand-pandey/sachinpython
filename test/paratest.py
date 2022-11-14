import time
from selenium import webdriver
from pageobjmodel.parapom import RegeLocators
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
class Loginpage():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(RegeLocators.url)
    driver.find_element(*RegeLocators.regestration).click()
    driver.find_element(*RegeLocators.firstname).send_keys(RegeLocators.first)
    driver.find_element(*RegeLocators.lastname).send_keys(RegeLocators.last)
    driver.find_element(*RegeLocators.address).send_keys(RegeLocators.add)
    driver.find_element(*RegeLocators.city).send_keys(RegeLocators.cit)
    driver.find_element(*RegeLocators.state).send_keys(RegeLocators.stat)
    driver.find_element(*RegeLocators.zipcode).send_keys(RegeLocators.zip)
    driver.find_element(*RegeLocators.phoneno).send_keys(RegeLocators.phone)
    driver.find_element(*RegeLocators.SSN).send_keys(RegeLocators.ss)
    driver.find_element(*RegeLocators.username).send_keys(RegeLocators.user)
    driver.find_element(*RegeLocators.PASSWORD).send_keys(RegeLocators.passw)
    driver.find_element(*RegeLocators.copassword).send_keys(RegeLocators.copass)
    driver.find_element(*RegeLocators.submit).click()
    time.sleep(4)
    driver.close()
