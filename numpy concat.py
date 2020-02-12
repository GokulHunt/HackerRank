# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 15:09:22 2019

@author: gs11
"""
#concat
import numpy
N, M, P = map(int, input().split())
N = numpy.array([input().split() for i in range(N)], int)
M = numpy.array([input().split() for i in range(M)], int)

print(numpy.concatenate((N, M), axis = 0))

#Floor ceil rint
import numpy
new_arr = numpy.array(input().split(), float)
print(numpy.floor(new_arr))
print(numpy.ceil(new_arr))
print(numpy.rint(new_arr))

#min and max
import numpy
n, m = map(int, input().split())
arr = numpy.array([input().split() for _ in range(n)], int)
mini = numpy.min(arr, axis = 1)
print(numpy.max(mini))

#dot and cross
import numpy
n = int(input())
A, B = [numpy.array([input().split() for _ in range(n)], int) for _ in range(2)]
print(numpy.dot(A, B))
print(numpy.cross(A, B))

#Inner and Outer
import numpy
A, B = [numpy.array(input().split(), int) for _ in range(2)]
print(numpy.inner(A, B))
print(numpy.outer(A, B))

#polynomial functions
import numpy
n = list(map(float,input().split()))
m = input()
print(numpy.polyval(n,int(m)))
