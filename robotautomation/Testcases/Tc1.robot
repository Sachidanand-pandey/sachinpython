*** Settings ***
Library  SeleniumLibrary



*** Variables ***




*** Test Cases ***
LoginTest
    create webdriver    chrome    executable_path="C:\Users\Fleek\Downloads\chromedriver_win32.exe"
    open browser    https://demo.nopcommerce.com/   chrome
    click link    Xpath:/html/body/div[6]/div[1]/div[1]/div[2]/div[1]/ul/li[2]/a
    close browser


*** Keywords ***