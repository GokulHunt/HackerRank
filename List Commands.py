# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 13:43:57 2019

@author: gs11
"""

L=[];
t=int(input());
for i in range(0,t):
    cmd=input().split();
    if cmd[0] == "insert":
        L.insert(int(cmd[1]),int(cmd[2]))
    elif cmd[0] == "append":
        L.append(int(cmd[1]))
    elif cmd[0] == "pop":
        L.pop();
    elif cmd[0] == "print":
        print(L)
    elif cmd[0] == "remove":
        L.remove(int(cmd[1]))
    elif cmd[0] == "sort":
        L.sort();
    else:
        L.reverse();
        
list = []
n = int(input())
for i in range(n):
    a = input().split()
    if len(a) == 3:
        eval("list." + a[0] + "(" + a[1] + "," + a[2] + ")")
    elif len(a) == 2:
        eval("list." + a[0] + "(" + a[1] + ")")
    elif a[0] == "print":
        print(list)
    else:
        eval("list." + a[0] + "()")