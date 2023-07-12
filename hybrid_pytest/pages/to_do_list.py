from selenium.webdriver.common.by import By
from pages.commonPage import commonOps
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

import time


class To_do_list:

    def __init__(self, driver):
        self.driver = driver


    to_do_click =(By.CSS_SELECTOR,"a[id='to-do-list'] h1")
    add_new_toDo =(By.CSS_SELECTOR,"input[placeholder='Add new todo']")
    hover1=(By.XPATH,"(//li[normalize-space()='Go to potion class'])[1]")
    del_1=(By.XPATH,"//li[normalize-space()='Go to potion class']//span")
    hover2=(By.XPATH,"//li[normalize-space()='Buy new robes']")
    del_2=(By.XPATH,"//li[normalize-space()='Buy new robes']//span")
    hover3=(By.XPATH,"//li[normalize-space()='Practice magic']")
    del_3=(By.XPATH,"//li[normalize-space()='Practice magic']//i[@class='fa fa-trash']")
    hover4=(By.XPATH,"//li[normalize-space()='SUPER']")
    del_4=(By.XPATH,"//li[normalize-space()='SUPER']//i[@class='fa fa-trash']")


    def to_do_list(self):
        commonOps.seleniumClick(self,self.to_do_click)
        commonOps.tab_handle(self,1)  
        commonOps.seleniumClick(self,self.add_new_toDo)
        #time.sleep(2)
        commonOps.seleniumSendKeys(self,self.add_new_toDo,"SUPER"+Keys.ENTER)
        commonOps.hover_mouse(self,self.hover1)
        commonOps.seleniumClick(self,self.del_1)

        commonOps.hover_mouse(self,self.hover2)
        commonOps.seleniumClick(self,self.del_2)

        commonOps.hover_mouse(self,self.hover3)
        commonOps.seleniumClick(self,self.del_3)

        commonOps.hover_mouse(self,self.hover4)
        commonOps.seleniumClick(self,self.del_4)

        time.sleep(1)
        commonOps.close_tab(self,1)
        commonOps.tab_handle(self,0)
