import pytest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from Utilities import configreader


@pytest.fixture(scope= "class")
def setup(request):
    driver = webdriver.Chrome()
    driver.get(configreader.readConfig("basic info","testsiteurl"))
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.implicitly_wait(5)
    #time.sleep(5)

    driver.close()