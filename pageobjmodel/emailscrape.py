import re
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get('https://www.randomlists.com/email-addresses?qty=1000')
page_source=driver.page_source
EMAIL_REGEX = r"[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?"
list_of_email = []
for re.match in re.finditer(EMAIL_REGEX,page_source):
    list_of_email.append(re.match.group())
for i, email in enumerate(list_of_email):
    print(f'{i+1}:{email}')
driver.close()
