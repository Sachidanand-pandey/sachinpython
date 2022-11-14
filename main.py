from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.get('https://www.google.com/')
driver.find_element(By.XPATH, '//input[@class="gLFyf gsfi"]').send_keys('david'+Keys.ENTER)
#a.send_keys('David')
#a.send_keys(Keys.ENTER)
a = driver.find_element(By.XPATH, '//div[@id="result-stats"]')
b = a.text
print(b)
c = b.split(' ')
print(c)
d = c[1].split(',')
m = "".join(d)
print(m)
print(int(m) > 500)
se = c[3].split('(')
print(se[1])
print(float(se[1]) < 1.0)
driver.close()
