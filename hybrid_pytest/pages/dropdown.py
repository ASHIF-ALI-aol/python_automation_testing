from selenium.webdriver.common.by import By
from pages.commonPage import commonOps
import time


class Dropdown:
    def __init__(self, driver):
        self.driver = driver


    drop_click=(By.XPATH,"//h1[normalize-space()='DROPDOWN, CHECKBOXE(S) & RADIO BUTTON(S)']")






    def drop_down_click(self):
        commonOps.seleniumClick(self,self.drop_click)
        commonOps.tab_handle(self,1)
        time.sleep(5)