'''
Created on Feb 27, 2016

@author: User
'''
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

class Application(object):
   

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def go_to_home_page(self):
        self.driver.get("http://localhost/php4dvd/")
    
    def login(self, user):
        driver = self.driver
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys(user.username)
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys(user.password)
        driver.find_element_by_name("submit").click()
    
def logout(self):
        driver = self.driver
        driver.find_element_by_link_text("Log out").click()
        driver.switch_to_alert().accept()

def is_logged_in(self):
    driver = self.driver
    try:
        self.wait.until(presence_of_element_located((By.CSS_SELECTOR, "nav")))
        return True
    except WebDriverException:
        return False

def is_not_logged_in(self):
    driver = self.driver
    try:
        self.wait.until(presence_of_element_located((By.ID, "loginform")))
        return True
    except WebDriverException:
        return False