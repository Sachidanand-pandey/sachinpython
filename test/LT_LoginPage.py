from test.LT_Login import LT_Login

username = "user-name@gmail.com"
password = "password"

class test_LT_LoginPage(webdriver_manager):
    def test_Login_Page(self):
        driver = self.driver
        self.driver.get("https://lambdatest.com/")
        lt_login_obj = LT_Login(driver)
        lt_login_obj.lt_login_user_name.send_keys(username)
        lt_login_obj.lt_login_password.send_keys(password)
        lt_login_obj.lt_login_button.click()
