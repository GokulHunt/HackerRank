# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 14:46:26 2019

@author: gs11
"""

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
arr = list(arr)
maxi = max(arr)
runner = max([arr[i] for i in range(len(arr)) if arr[i] < max(arr)])
print(runner)