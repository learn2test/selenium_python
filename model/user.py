'''
Created on Feb 27, 2016

@author: User
'''
from MySQLdb.constants.ER import PASSWORD_ANONYMOUS_USER

class User(object):
    
    @classmethod
    def Admin(cls):
        return cls(username="admin", password="admin")


    def __init__(self, username=None, password=None, email=None):
        self.username = username
        self.password = password
        self.email = email
        