# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 02:22:17 2021

@author: Meem
"""

def palindrome(x, start, size):
    t=True
    temp=[0]*len(x)
    temp=x
    s=start
    index=(start+size-1)%len(x)
    for i in range(0, size):
        if(temp[s]==x[index]):
            t=True
            s+=1
            if(s>=len(x)):
                s=0
            index=(index-1)%len(x)
        else:
            t=False
            break
    return t
source=[20,10,0,0,0,10,20,30]
print(palindrome(source, 5, 5))
