from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://app.thomsondigital2021.com/login')
time.sleep(1.5)
textbox = driver.find_element(By.XPATH, "//*[@id='mobile_num']")
textbox.send_keys("8957370083")
time.sleep(3)
driver.find_element(By.XPATH, "//*[@id='mobile-input-btn']").click()
time.sleep(2)
box =driver.find_element(By.XPATH, "//*[@id='testing_otp']")
driver.execute_script("arguments[0].setAttribute('class','')", box)
val = box.text
print(val)
time.sleep(1)
a =driver.find_element(By.XPATH, "//input[@id='opt_one']")
a.send_keys(val)
a.send_keys(Keys.ENTER)
time.sleep(3)
driver.find_element(By.XPATH, '//a[@class="openSharefrnd ref_class"]').click()
time.sleep(3)
driver.find_element(By.XPATH, '//input[@id="referEmails"]').send_keys('ai3f9@gmail.com')
time.sleep(4)
driver.find_element(By.XPATH, "//button[text()=' Send Invite']").click()
time.sleep(4)
b = driver.find_element(By.XPATH, '//*[@id="referedfrnd"]/div/div/div/div[2]/div[2]/p')
c = b.text
print(c)
if c =="Invitation sent!":
    print('pass')
else:
    print('false')
