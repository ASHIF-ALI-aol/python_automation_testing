import pytest
#from selenium import webdriver
#import time
#from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from Utilities.BaseClass import BaseClass
#from pages.commonPage import commonOps
from pages.fillingform import fillform
from pages.login_portal import LogIn
from pages.button_clicks import Button_clicks
from pages.to_do_list import To_do_list
from pages.accordian import Accordian
from pages.dropdown import Dropdown
from Utilities.DataProvider import DataProvider



class TestOne(BaseClass):
    def test_one(self, getData):
        fill= fillform(self.driver)
        fill.loginTOApplication(getData)
        # tab handler
        # commonOps.tab_handle(1)      



    @pytest.fixture(params=DataProvider.get_data("Testcase1"))
    def getData(self, request):
        return request.param
    

    def test_two(self,getData):
        logg = LogIn(self.driver)
        logg.click_login(getData)

    def test_three(self):
        buttons = Button_clicks(self.driver)
        buttons.click_button()
        

    def test_four(self):
        to_do = To_do_list(self.driver)
        to_do.to_do_list()


    def test_five(self):
        app_dpp_text=Accordian(self.driver)
        app_dpp_text.accordian_textEffects()
        

    def test_six(self):
        drop_down=Dropdown(self.driver)
        drop_down.drop_down_click()
        

        
       

  
        

      
      