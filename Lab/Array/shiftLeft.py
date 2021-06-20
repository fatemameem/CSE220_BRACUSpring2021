# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 13:15:39 2021

@author: Meem
"""

def shiftLeft(source, k):
    i=0
    while(i<k):
        source[i]=source[i+k]
        i=i+1
    i=len(source)-1
    while(i>=k):
        source[i]=0
        i=i-1

s=[10,20,30,40,50,60]
shiftLeft(s, 3)
print(s)