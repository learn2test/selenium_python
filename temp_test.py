'''
Created on Feb 27, 2016

@author: User
'''
from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://localhost/php4dvd")
driver.implicitly_wait(10)
driver.find_element_by_id("username").clear()
driver.find_element_by_id("username").send_keys("admin")
driver.find_element_by_name("password").send_keys("admin")
driver.find_element_by_name("submit").click()