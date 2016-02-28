'''
Created on Feb 27, 2016

@author: User
'''
from selenium import webdriver
from selenium.common.exceptions import *
from selenium_fixture import app
from model.user import User




def test_login(app):
    app.driver.get("http:localhost/php4dvd/")
    login(app.driver, User.Admin())
    logout(app.driver)

def login(driver, user):
    driver.find_element_by_id("username").clear()
    driver.find_element_by_id("username").send_keys(user.username)
    driver.find_element_by_name("password").clear()
    driver.find_element_by_name("password").send_keys(user.password)
    driver.find_element_by_name("submit").click()
    
def logout(driver):
    driver.find_element_by_link_text("Log out").click()
    driver.switch_to_alert().accept()
   
    

