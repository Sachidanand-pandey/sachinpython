class WebDriverSetup():
    def chrome(self):
        from selenium import webdriver
        from webdriver_manager.chrome import ChromeDriverManager
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
w=WebDriverSetup()
w.chrome()