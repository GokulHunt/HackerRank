# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 13:39:01 2019

@author: gs11
"""

def rem_duplicates(string)   :
    new = ''
    for ch in string:
        if ch not in new:
            new += ch
    return new

def merge_the_tools(string, k):
    # your code goes here
    s = string
    n = len(s)
    r = int(n/k)
    l = []
    for i in range(1, r+1):
        l.append(s[(i-1)*k : i*k])
    u = []
    for i in l:
        u.append(rem_duplicates(i))
    return u
    

def merge_the_tools2(string, k):
    len_of_u_string = int(k)
    len_of_full_string = len(string)
    u_tmp = []
    i = 0
    for i in range(0,len(string),int(k)):
        tmp_str = string[i:i+len_of_u_string]
        tmp_str = rem_duplicates(tmp_str)
        print(tmp_str)
        u_tmp.append(tmp_str)

    return 0
    

         