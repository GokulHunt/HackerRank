# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 15:42:05 2019

@author: gs11
"""

import numpy as np
n, m = map(int, input().split())
array = np.array([input().strip().split() for _ in range(n)], int)
print (array.transpose())
print (array.flatten())