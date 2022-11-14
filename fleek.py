from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
import pyautogui
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get('https://www.google.com/')
a = driver.find_element(By.XPATH, '//input[@class="gLFyf gsfi"]')
a.send_keys('software testing')
a.send_keys(Keys.ENTER)
pyautogui.hotkey('ctrl', 'f')
pyautogui.write('fleek it solution')
time.sleep(5)
driver.close()