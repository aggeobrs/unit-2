# -*- coding: utf-8 -*-
"""Quiz#009

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JDHiPxXsaw2VH4awtxulVwH1hmeayZ-C
"""

def missingNumber(list1):
    missing = 0
    for i in range(list1[0], list1[-1]+1):
        if i not in list1:
            missing = i
    return missing

print(missingNumber(([1, 2, 3, 5, 6, 7])))
print(missingNumber([4, 5, 6, 8, 9, 10]))
print(missingNumber([73, 74, 75, 76, 78, 79]))