# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 11:59:36 2021

@author: Meem
"""

def repetition(x):
    freq=[None]*len(x)
    # visited=0
    for i in range(0, len(x)):
        count=1
        for j in range(i+1, len(x)):
            if(x[i]==x[j]):
                count+=1
                freq[j]=0
            if(freq[i]!=0):
                freq[i]=count
    for i in range(0, len(freq)):
        count=1
        for j in range(i+1, len(freq)):
            if(freq[i]==freq[j]):
                if(freq[i]!=1 and freq[i]!=0):
                    return True
                else:
                    return False
source=[3,4,6,3,4,7,4,6,8,6,6]
t=repetition(source)
print(t)