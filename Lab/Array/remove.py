# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 14:01:52 2021

@author: Meem
"""

def remove(source, size, idx):
    for i in range(len(source)-1):
        if(i==idx):
            source[i]=0
    for i in range(idx, len(source)-1):
        source[i]=source[i+1]
    source[size-1]=0

source=[10,20,30,40,50,0,0]
remove(source, 5, 2)
print(source)