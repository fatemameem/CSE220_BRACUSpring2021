# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 23:15:46 2021

@author: Meem
"""

def arraySeries(n):
    a=[None]*n*n
    count=n
    index=len(a)-1
    while(count>0):
        for i in range(1,n+1):
            if(i<=count):
                a[index]=i
            else:
                a[index]=0
            index-=1
        count-=1
    return a
source=arraySeries(5)
print(source)