# -*- coding: utf-8 -*-
"""Quiz#012

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qeaLGuDUa8XECIDLE4Au3MGymD45f5IJ
"""

def wordlength(list1):
  S=0
  for i in range(len(list1)):
    S+= len(list1[i])
  Average = S/len(list1)
  return Average

print(wordlength(["home", "car", "travel", "beach"]))