from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://www.tutorialspoint.com/about/about_careers.htm")
driver.refresh()
a = ActionChains(driver)
a.key_down(Keys.CONTROL).send_keys('F').key_up(Keys.CONTROL).perform()
driver.close()