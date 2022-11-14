class sachin():
    def chrome_setup():
        from selenium import webdriver
        import time
        import pyautogui
        from selenium.webdriver.common.by import By
        from webdriver_manager.chrome import ChromeDriverManager
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        return driver




'''driver=chrome_setup()
driver.get('https://rahulshettyacademy.com/seleniumPractise/#/')
driver.maximize_window()'''
