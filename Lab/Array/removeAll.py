# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 19:40:34 2021

@author: Meem
"""

def removeAll(source, size, element):
    temp=[]
    for i in range(size):
        if(source[i]!=element):
            temp.append(source[i])
        source[i]=0
    for i in range(len(temp)):
        source[i]=temp[i]

source=[10,2,30,2,50,2,2,0]
removeAll(source, 7, 2)
print(source)