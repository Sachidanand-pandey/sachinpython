from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.get('https://www.amazon.in/')
#capture cokies
coolies=driver.get_cookies()
print(len(coolies))
print(coolies)
#add new cookies
cookies={'name':'my cookies','value':'632700200098'}
driver.add_cookie(cookies)
coolies=driver.get_cookies()
print(len(coolies))
print(coolies)
driver.delete_cookie('my cookies')
coolies=driver.get_cookies()
print(len(coolies))
print(coolies)
cookies={'name':'cookies','value':'2700200098'}
driver.add_cookie(cookies)
coolies=driver.get_cookies()
print(len(coolies))
print(coolies)
