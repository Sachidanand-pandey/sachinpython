import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
def setUpModule():
    print('set up module')
def tearDownModule():
    print('tear down module')
class testtitle(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    def tearDown(self):
        self.driver.close()
    @classmethod
    def setUpClass(cls):
        print('application test start')
    @classmethod
    def tearDownClass(cls):
        print('application test stop')
    def testgoogle(self):
        self.driver.get('https://www.google.com/')
        print("Title of the page is:"+self.driver.title)
    def testbing(self):
        self.driver.get('https://www.bing.com/')
        print("Title of the page is:"+self.driver.title)
    def testamazon(self):
        self .driver.get('https://www.amazonn.com/')
        print("title of the page is:"+self.driver.title)
    @unittest.SkipTest
    def testflipkart(self):
        self.driver.get('https://www.flipkart.com/')
        print("title of the page is:"+self.driver.title)
    @unittest.skip('skip this test cases')
    def testecom(self):
        self.driver.get('https://demo.nopcommerce.com/')
        print("title of the page is:"+self.driver.title)
    @unittest.skipIf(1==1,'skipped if condition is true')
    def testeco(self):
        self.driver.get('https://www.myntra.com/')
        print("This is the title of the page:"+self.driver.title)
    if __name__ == "__main__":
        unittest.main()
