import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
s=driver.get('http://tutorialsninja.com/demo/index.php?route=product/search&search=macbook')
get_url = driver.current_url
get_url
if a=='http://tutorialsninja.com/demo/index.php?route=product/search&search=macbook':
    print('pass')
else:
    print('failed')
