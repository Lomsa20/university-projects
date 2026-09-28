# -*- coding: utf-8 -*-
"""
Created on Sun Oct 19 15:53:44 2025

@author: mylaptop.ge
"""
grade = int(input("Enter Your Grade: "))
income = int(input("Enter Your Family Income: "))

if 1<= grade <= 5:
    if income < 15000:
        print("Free Lunch")
    elif income < 25000:
        print("Discounted Lunch")
    else: 
        print("Full Price")
if 6<= grade <= 12:
    if income < 12000:
        print("Free lunch")
    elif 12000 <income < 20000:
        print("Dicounted Lunch")
    else:
        print("Full price")