# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 17:19:00 2019

@author: gs11
"""
students = []
for _ in range(int(input())):
        name = input()
        score = float(input())
        row =[name, score]
        students.append(row)
grades = min([students[i][1] for i in range(len(students))])
low_grade = min([students[i][1] for i in range(len(students)) if students[i][1] > grades ])
lowest = sorted([students[i][0] for i in range(len(students)) if students[i][1] == low_grade])
print('\n'.join(lowest))