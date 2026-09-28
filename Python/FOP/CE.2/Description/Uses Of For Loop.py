# -*- coding: utf-8 -*-
"""
Created on Tue Oct 21 23:24:04 2025

@author: mylaptop.ge
"""
#The for loop in Python is used to iterate the statements or a part of the program several times. It is
#frequently used to traverse the data structures like list, tuple, or dictionary.
n= int(input("enter n row: "))
for j in range (0,n):
    for k in range (0,j+1):
        print("%", end= "")
    print()
    # So after each .append(), the list grows