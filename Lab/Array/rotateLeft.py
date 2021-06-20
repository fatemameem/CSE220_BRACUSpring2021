# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 13:55:09 2021

@author: Meem
"""

def rotateLeft(source, k):
    temp=0;
    while(k>0):
        temp=source[0]
        for i in range(len(source)-1):
            source[i]=source[i+1]
        source[len(source)-1]=temp
        k=k-1

s=[10,20,30,40,50,60]
rotateLeft(s, 3)
print(s)