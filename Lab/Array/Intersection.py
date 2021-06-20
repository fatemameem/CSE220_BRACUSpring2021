# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 03:07:35 2021

@author: Meem
"""

def intersection(x, start_x, size_x, y, start_y, size_y):
    x=linearize(x, start_x, size_x)
    y=linearize(y, start_y, size_y)
    temp=[]
    for i in range(0,len(x)):
        for j in range(0, len(y)):
            if(x[i]==y[j]):
                temp.append(x[i])
    return temp

def linearize(x, start, size):
    temp=[0]*size
    p=start
    for i in range(0,len(temp)):
        if(x[p]!=0):
            temp[i]=x[p]
            p=(p+1)%len(x)
    return temp
a1=[40,50,0,0,0,10,20,30]
a2=[10,20,5,0,0,0,0,0,5,40,15,25]
r=intersection(a1,5,5,a2,8,7)
print(r)