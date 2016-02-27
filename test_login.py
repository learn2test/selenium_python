'''
Created on Feb 27, 2016

@author: User
'''
from selenium import webdriver
from selenium.common.exceptions import *
import unittest



class Untitled(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.base_url = "http://localhost/"
        self.verificationErrors = []
        self.accept_next_alert = True
        
    def test_untitled(self):
        driver = self.driver
        driver.get(self.base_url + "php4dvd/")
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("admin")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("admin")
        driver.find_element_by_name("submit").click()
        
    def tearDown(self):
        self.driver.quit()

suite = unittest.TestLoader().loadTestsFromTestCase(Untitled)
unittest.TextTestRunner(verbosity=2).run(suite)


