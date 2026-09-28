# -*- coding: utf-8 -*-
"""
Created on Sun Nov  9 01:59:16 2025

@author: mylaptop.ge
"""

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
unique = (a != 0.0)
infinite = (a == 0.0) and (b == c)
none = (a == 0.0) and (b != c)
x = ((c - b) / a) * float(unique)
print(unique)
print(infinite)
print(none)
print(x)
