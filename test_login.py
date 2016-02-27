'''
Created on Feb 27, 2016

@author: User
'''
from selenium import webdriver
from selenium.common.exceptions import *
import unittest
from selenium_fixture import driver



def test_login(driver):
    driver.get("http:localhost/php4dvd/")
    login(driver)
    logout(driver)

def login(driver, username, password):
    driver.find_element_by_id("username").clear()
    driver.find_element_by_id("username").send_keys("admin")
    driver.find_element_by_name("password").clear()
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("submit").click()
    
def logout(driver):
    driver.find_element_by_link_text("Log out").click()
    driver.switch_to_alert().accept()
   
    

