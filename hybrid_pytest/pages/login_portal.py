from selenium.webdriver.common.by import By
from pages.commonPage import commonOps
from selenium.webdriver.common.alert import Alert
import time

class LogIn:

    def __init__(self, driver):
        self.driver = driver

    login= (By.CSS_SELECTOR,"a[id='login-portal'] h1")
    username =(By.XPATH,"//input[@id='text']")
    password = (By.XPATH,"//input[@id='password']")
    login_button =(By.XPATH,"//button[@id='login-button']")

    
    def click_login(self, getData):
        commonOps.seleniumClick(self,self.login)
        commonOps.tab_handle(self,1)
        commonOps.seleniumSendKeys(self,self.username,getData["Firstname"])
        commonOps.seleniumSendKeys(self,self.password,getData["Lastname"])
        commonOps.seleniumClick(self,self.login_button)
        commonOps.alert_handle(self)
        commonOps.close_tab(self,1)
        commonOps.tab_handle(self,0)
        
    

