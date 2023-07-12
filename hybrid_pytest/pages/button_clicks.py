from selenium.webdriver.common.by import By
from pages.commonPage import commonOps
from selenium.webdriver.common.action_chains import ActionChains
import time


class Button_clicks:

    def __init__(self, driver):
        self.driver = driver

    btn_click =(By.XPATH,"//h1[normalize-space()='BUTTON CLICKS']")
    first_btn =(By.ID,"button1")
    second_btn=(By.XPATH,"//span[@id='button2']")
    third_btn=(By.XPATH,"//span[@id='button3']")
    pop_up = (By.XPATH,"//div[@id='myModalClick']//button[@type='button'][normalize-space()='Close']")
    pop_up2= (By.XPATH,"//div[@class='modal-dialog modal-md']//button[@type='button'][normalize-space()='Close']")
    pop_up3= (By.XPATH,"(//button[@type='button'][normalize-space()='Close'])[3]")

    def click_button(self):
        commonOps.seleniumClick(self,self.btn_click)        
        commonOps.tab_handle(self,1)
        commonOps.seleniumClick(self,self.first_btn)
        time.sleep(1)       
        commonOps.seleniumClick(self,self.pop_up)
        commonOps.seleniumClick(self,self.second_btn)
        time.sleep(1)
        commonOps.seleniumClick(self,self.pop_up2)
        
        commonOps.seleniumClick(self,self.third_btn)
        time.sleep(1)
        commonOps.seleniumClick(self,self.pop_up3)
        time.sleep(1)
        commonOps.close_tab(self,1)
        commonOps.tab_handle(self,0)

      