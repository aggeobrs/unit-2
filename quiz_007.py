# -*- coding: utf-8 -*-
"""Quiz#007

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JDHiPxXsaw2VH4awtxulVwH1hmeayZ-C
"""

def letters(n):
    for i in range(0, len(n)):
            print(str(i) + "->" + str(n[i]))

print(letters("hello"))