# -*- coding: utf-8 -*-
"""
Created on Tue Oct 28 09:05:11 2025

@author: mylaptop.ge
"""

class Parent:
    def method(self):
        print("parent method 1") # This can be transferd in child class
    
    def __method2(self): # __ this mean method 2 is private and it will be only in parent class 
        print("parent method 2")
    
class Child(Parent):
    pass
Child1 = Child()


