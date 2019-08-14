# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 20:00:31 2019

@author: gokul
"""

def is_leap(year):
    leap = False

    # Write your logic here
    if year < 100:
        if year % 4 == 0:
            leap = True
    if year > 100:
        if year % 4 == 0:
            if year % 100 == 0 and year % 400 != 0:
                leap = False
            else:
                leap = True


    return leap
