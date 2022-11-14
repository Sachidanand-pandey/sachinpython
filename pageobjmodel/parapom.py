from selenium.webdriver.common.by import By
class RegeLocators(object):
    first = 'sachin'
    last = 'pandey'
    add = 'sector15'
    cit = 'noida'
    stat = 'UttarPradesh'
    zip = '2725001'
    phone = '8678954'
    user = 'bankpage'
    passw = 'Pandey@123'
    copass = 'Pandey@123'
    ss = '2345'
    url="https://parabank.parasoft.com/parabank/index.htm"
    regestration=(By.XPATH,"//div[@id='loginPanel']/p[2]/a")
    firstname=(By.XPATH,'//input[@id="customer.firstName"]')
    lastname=(By.XPATH,'//input[@id="customer.lastName"]')
    address=(By.XPATH,'//input[@id="customer.address.street"]')
    city=(By.XPATH,'//input[@id="customer.address.city"]')
    state=(By.XPATH,'//input[@id="customer.address.state"]')
    zipcode=(By.XPATH,'//input[@id="customer.address.zipCode"]')
    phoneno=(By.XPATH,'//input[@id="customer.phoneNumber"]')
    SSN=(By.XPATH,'//input[@id="customer.ssn"]')
    username= (By.XPATH, '//input[@id="customer.username"]')
    PASSWORD= (By.XPATH,'//input[@id="customer.password"]')
    copassword= (By.XPATH, '//input[@name="repeatedPassword"]')
    submit=(By.XPATH,'//input[@value="Register"]')
class loginlocator(object):
    user = 'bankpages'
    pwss = 'Pandey@123'
    url = "https://parabank.parasoft.com/parabank/index.htm"
    usernam='//input[@type="text"]'
    passwor='//input[@name="password"]'
    button='//input[@value="Log In"]'