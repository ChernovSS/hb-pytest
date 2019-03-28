# -*- coding: utf-8 -*-

class Account:
    def __init__(self, username=None, email=None, emplyeeuri=None, isenable=None):
       self.username=username
       self.email=email
       self.emplyeeuri=emplyeeuri
       self.isenable=isenable


    def __repr__(self):
        return "%s:%s:%s:%s:" % (self.username, self.email, self.emplyeeuri, self.isenable)

