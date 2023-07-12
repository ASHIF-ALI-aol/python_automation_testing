from selenium.webdriver.common.by import By
from Utilities import configreader
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service


import time



class commonOps:

    def __init__(self, driver):
        self.driver = driver   

    

    def tab_handle (self, val):
        windows = self.driver.window_handles

        for window in windows:
          print(window)
        return self.driver.switch_to.window(self.driver.window_handles[val])
    
    def close_tab(self,id):
        self.driver.close()
    

    def alert_handle(self):
        alert = self.driver.switch_to.alert               
        alert.accept()
        time.sleep(2)

    def seleniumClick(self,locator):
        self.driver.find_element(*locator).click()
    
    def seleniumSendKeys(self,locator,value):
        self.driver.find_element(*locator).send_keys(value)
    
    def seleniumSelect(self,locator,text):
        sel=Select(self.driver.find_element(locator))
        sel.select_by_visible_text(text)   
    
    def hover_mouse(self,locator):
        hoverable = self.driver.find_element(*locator)
        ActionChains(self.driver)\
        .move_to_element(hoverable)\
        .perform()

    def mouse_offset(self,val1,val2):
        ActionChains(self.driver)\
        .move_by_offset( val1, val2)\
        .click()