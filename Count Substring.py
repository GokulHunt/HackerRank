# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 19:50:57 2019

@author: gokul
"""

def count_substring(string, sub_string):
    s = string
    ls = len(s)
    ss = sub_string
    lss = len(ss)
    count = 0
    for i in range(0, ls):
        if s[i] == ss[0]:
            if s[i:i+lss] == ss:
                count += 1

    return count
