# -*- coding: utf-8 -*-
"""
Created on Tue Oct 21 22:10:03 2025

@author: mylaptop.ge
"""

while True:
    membership = input("Enter your membership type(Standard, Premium, Elite): ").lower()
    if membership in ["standard", "premium", "elite"]:
        break
    else:
        print("You entered an incorrect type of membership.")

while True:
    student = input("Are you a student?(Yes/No): ").lower()
    if student in ["yes", "no"]:
        break
    else:
        print("You spelled it wrong.")

if membership == "standard":
    if student == "yes":
        print("Your monthly payment will be $25.")
    else:
        print("Your monthly payment will be $30.")

elif membership == "premium":
    if student == "yes":
        print("Your monthly payment will be $40.")
    else:
        print("Your monthly payment will be $50.")

elif membership == "elite":
    if student == "yes":
        print("Your monthly payment will be $60.")
    else:
        print("Your monthly payment will be $70.")
        
        
        