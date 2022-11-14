import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407')
s = driver.find_element(By.XPATH,'//input[@id="RESULT_FileUpload-10"]')
time.sleep(5)
s.send_keys('C:\Program Files (x86)\image\logo.jpg')
time.sleep(5)
driver.close()
