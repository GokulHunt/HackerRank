# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def minion_game(string):
    # your code goes here
    vowels = 'AEIOU'
    Kevin = 0
    Stuart = 0
    for i in range(len(string)):
        if string[i] in vowels:
            Kevin += (len(string)-i)
        else:
            Stuart += (len(string)-i)
    if Kevin > Stuart:
        print("Kevin", Kevin)
    elif Stuart > Kevin:
        print("Stuart", Stuart)
    else:
        print("Draw")