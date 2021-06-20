# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 21:21:58 2021

@author: Meem
"""
 
def splitArray(source) :
	left=0
	for i in range(0, len(source)) : 
		left =left+source[i] 
		right= 0
		for j in range(i+1, len(source)) : 
			right=right+source[j]
		if (left==right) : 
			return True
	return False

source = [2,1,1,2,1] 
s=splitArray(source)
if(s==True):
    print("true")
else:
    print("false")