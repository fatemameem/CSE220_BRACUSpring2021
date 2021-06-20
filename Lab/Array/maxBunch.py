# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 00:30:54 2021

@author: Meem
"""

def maxBunch(s):
    bunch=1
    maxbunch=0
    for i in range(len(s)-1):
        if(s[i]==s[i+1]):
            bunch+=1
            if(bunch>maxbunch):
                maxbunch=bunch
        else:
            bunch=1
    if(maxbunch>1):
        return maxbunch
    else:
        return 0
source=[1,1,2,2,1,1,1,1]
print(maxBunch(source))