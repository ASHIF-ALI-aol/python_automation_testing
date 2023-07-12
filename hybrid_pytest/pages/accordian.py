from selenium.webdriver.common.by import By
from pages.commonPage import commonOps
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class Accordian:

    def __init__(self, driver):
        self.driver = driver

    accordian_click =(By.XPATH,"//h1[normalize-space()='ACCORDION & TEXT AFFECTS (APPEAR & DISAPPEAR)']")
    manual_test=(By.XPATH,"//button[@id='manual-testing-accordion']")
    cucumber=(By.XPATH,"//button[@id='cucumber-accordion']")
    automation=(By.XPATH,"//button[@id='automation-accordion']")
    keepclicking=(By.XPATH,"//button[@id='click-accordion']")
    

    def accordian_textEffects(self):


        commonOps.seleniumClick(self,self.accordian_click)        
        commonOps.tab_handle(self,1)
        commonOps.seleniumClick(self,self.manual_test) 
        time.sleep(2)
        commonOps.seleniumClick(self,self.manual_test) 
        commonOps.seleniumClick(self,self.cucumber) 
        time.sleep(2)
        commonOps.seleniumClick(self,self.cucumber) 
        commonOps.seleniumClick(self,self.automation) 
        time.sleep(2)
        commonOps.seleniumClick(self,self.automation)
        commonOps.seleniumClick(self,self.keepclicking)
        time.sleep(10)
        #commonOps.seleniumClick(self,self.keepclicking)
        commonOps.seleniumClick(self,self.keepclicking)
        time.sleep(2)
        commonOps.seleniumClick(self,self.keepclicking)                
        commonOps.close_tab(self,1)
        commonOps.tab_handle(self,0)

        






