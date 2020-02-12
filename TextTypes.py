# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 18:52:36 2019

@author: gs11
"""

s = '123'
res = False
for c in s:
    if c.isalnum() == True:
        res = True
        break
print(res)
res = False
for c in s:
    if c.isalpha() == True:
        res = True
        break
print(res)
res = False
for c in s:
    if c.isdigit() == True:
        res = True
        break
print(res)
result = False
for c in s:
    if c.islower() == True:
        result = True
        break
print(result)
result = False
for c in s:
    if c.isupper() == True:
        result = True
        break
print(result)
