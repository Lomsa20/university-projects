# -*- coding: utf-8 -*-
"""
Created on Fri Oct 17 21:11:03 2025

@author: mylaptop.ge
"""
while True:
    plan = input("Enter your plan type (basic, standard, premium): ").lower()
    
    if plan in ["basic", "standard", "premium"]:
        break   # Exit loop when plan is valid
    else:
        print("Invalid plan type. Please try again Or go on ;).")

# Continue program after valid plan
usage = float(input("Enter your data usage in GB: "))

if plan == "basic":
    if usage > 5:
        print("Over limit")
    else:
        print("Usage Badass")

elif plan == "standard":
    if usage > 10:
        print("Over limit")
    else:
        print("your Usage is OK ma man")

elif plan == "premium":
    if usage > 20:
        print("you Over limit bro")
    else:
        print("you use good ma brothaa")