# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""



#reversing an array: in place

def reverse(source):

    i=0 #pointer at 0th index of source

    j=len(source)-1 #pointer at last index of source

    while(i<j):

        temp=source[i] #swapping the first and last elements

        source[i]=source[j]

        source[j]=temp

        i=i+1

        j=j-1



a=[10,20,30,40,50]

reverse(a)

print(a)

