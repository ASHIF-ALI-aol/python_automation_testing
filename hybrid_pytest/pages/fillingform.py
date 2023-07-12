from selenium.webdriver.common.by import By
from pages.commonPage import commonOps



class fillform:

    def __init__(self, driver):
        self.driver = driver


    contact =(By.CSS_SELECTOR,"a[id='contact-us'] h1")
    firstname =(By.XPATH,"//input[@placeholder='First Name']")
    lastname = (By.XPATH,"//input[@placeholder='Last Name']")
    email = (By.XPATH,"//input[@placeholder='Email Address']")
    comments = (By.XPATH,"//textarea[@placeholder='Comments']")
    reset =(By.XPATH,"//input[@value='RESET']")
    submit = (By.XPATH,"//input[@value='SUBMIT']")

    def loginTOApplication(self,getData):
        commonOps.seleniumClick(self,self.contact)
        commonOps.tab_handle(self,1)
        commonOps.seleniumSendKeys(self,self.firstname,getData["Firstname"])
        commonOps.seleniumSendKeys(self,self.lastname,getData['Lastname'])
        commonOps.seleniumSendKeys(self,self.email,getData['EmailAddresss'])
        commonOps.seleniumSendKeys(self,self.comments,getData['Comments'])
        commonOps.seleniumClick(self,self.reset)
        commonOps.seleniumSendKeys(self,self.firstname,'username')
        commonOps.seleniumSendKeys(self,self.lastname,'lastname')
        commonOps.seleniumSendKeys(self,self.email,'username@gmail.com')
        commonOps.seleniumSendKeys(self,self.comments,'commentssssssss')
        commonOps.seleniumClick(self,self.submit)
        commonOps.close_tab(self,1)        
        commonOps.tab_handle(self,0)
        

    #def click_contact(self):
    #    return self.driver.find_element(*fillform.contact)
    
    #def first_name(self):
    #    return self.driver.find_element(*fillform.firstname)
    
    #def last_name(self):
    #    return self.driver.find_element(*fillform.lastname)
    
    #def email_address(self):
    #    return self.driver.find_element(*fillform.email)
    
    #def comments_a(self):
    #    return self.driver.find_element(*fillform.comments)
    
    #def reset_a(self):
    #    return self.driver.find_element(*fillform.reset)
    
    #def submit_a(self):
    #    return self.driver.find_element(*fillform.submit)
    
   