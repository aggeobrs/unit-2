# -*- coding: utf-8 -*-
"""Quiz#014

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1X5-6yTmJ7M5eZsg5TDypVOZ9gp54iIQE
"""

def evenlySpaced(a, b, c):
  max=a
  if b>max:
    max=b
  if c>max:
    max=c
  if a!=max:
    min1=a
    if min1>b:
      min1=b
    if min1>c:
      min1=c
  else:
    if b>c:
      c=min1
    else:
      b=min1
  med= a+b+c-max-min1
  if max-med==med-min1:
    statement=True
  else:
    statement=False
  return statement

print(evenlySpaced(2,4,6))
print(evenlySpaced(4,6,2))
print(evenlySpaced(4,6,3))