# -*- coding: utf-8 -*-
"""Quiz#006

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JDHiPxXsaw2VH4awtxulVwH1hmeayZ-C
"""

def MixStart(n):
    out = 'FALSE'
    if n[1:3] =='ix':
        out="TRUE"
    return out

print(MixStart('mix snacks'))
print(MixStart('pix snacks'))
print(MixStart('piz snacks'))