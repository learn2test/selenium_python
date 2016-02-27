'''
Created on Feb 27, 2016

@author: User
'''

from selenium import webdriver
import pytest

@pytest.fixture
def driver(request):
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    request.addfinalizer(driver.quit)
    return driver