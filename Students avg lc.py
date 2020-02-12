# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 17:52:33 2019

@author: gs11
"""

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
average = [sum(student_marks[std])/len(student_marks[std]) for std in student_marks if student_marks[std] == student_marks[query_name]]
avg = ''.join(str(e) for e in average)
print("%.2f" % float(avg))

