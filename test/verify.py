from pageobjmodel.homepage import Homepage
from pageobjmodel.downlod import sachin
driver=sachin.chrome_setup()
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pyautogui
driver.maximize_window()
driver.get(Homepage.login)
a = driver.find_element(By.XPATH, Homepage.search)
a.send_keys('software testing')
print(a.is_enabled())
print(a.is_displayed())
a.send_keys(Keys.ENTER)
pyautogui.hotkey('ctrl', 'f')
pyautogui.write('fleek it solutions')
driver.get_screenshot_as_file("screenshot.png")
time.sleep(5)
driver.close()