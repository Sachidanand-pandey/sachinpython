from test.page import Mainpage
from test.page import Loginpage
from test.page import Logoutpage
def test_sign_in_with_valid_user(self):
    mainpage = Mainpage(self.driver)
    mainpage.Click_myaccount()
    loginpage=Loginpage(self.driver)
    loginpage.login("bpb@bpb.com","bpb@123")
    logoutpage=Logoutpage(self.driver)
    logoutpage.logout()