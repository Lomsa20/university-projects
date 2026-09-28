# -*- coding: utf8 -*-
"""
Created on Fri Oct 17 21:23:33 2025

@author: mylaptop.ge
"""
while True:
    service = input("Enter your Quality type.(poor,avarege or excellent): ").lower()
    if service in ["poor","avarege", "excellent"]:
        break
    else:
        print("Your Service Type is invalid. PLS Try again or Dont DISTURB ME...")
        
bill = int(input("Enter Your Wasted money: "))
if service == "poor":
    tip_percent = 5
if service == "avarege":
    if bill < 50 :
        tip_percent = 10 
    else:
        tip_percen = 12
if service == "excellent":
    if bill < 50 :
        tip_percent = 15
    else:
        tip_percent = 19 
#calculate tip and total
tip = bill * tip_percent / 100   
total = bill + tip 
#show results
print("\n--- BILL SUMMARY ---")
print(f"Service quality: {service.capitalize()}")
print(f"Bill amount: {bill:.2f} $")
print(f"Tip percentage: {tip_percent}%")
print(f"Tip amount: {tip:.2f} $")
print(f"Total to pay: {total:.2f} $")
print("----------------------")