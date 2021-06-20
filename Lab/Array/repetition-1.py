# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 11:44:35 2021

@author: Meem
"""

def repetition(arr):
    #Array fr will store frequencies of element  
    fr = [None] * len(arr);  
    visited = -1;  
   
    for i in range(0, len(arr)):  
        count = 1;  
        for j in range(i+1, len(arr)):  
            if(arr[i] == arr[j]):  
                count = count + 1;  
            #To avoid counting same element again  
                fr[j] = visited;  
              
                if(fr[i] != visited):  
                    fr[i] = count;  
    for i in range(len(fr)-1):
        print(fr[i])
    

s=[4,5,6,6,4,3,6,4]
repetition(s)