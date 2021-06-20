# -*- coding: utf-8 -*-
"""
Created on Sun May  2 05:57:48 2021

@author: Meem
"""

# def alternatingCharacters(s):
#     # Write your code here
#     for i in range(len(s)):
#         for j in range(i):
#             if(s[i]==s[j]):
#                 print(True)
        

# alternatingCharacters("QWEERTY")

def sockMerchant(n, ar):
    # Write your code here
    count=0
    # pair=0
    for i in range(n):
        temp=ar[i]
        for j in range(n-1):
            if temp==ar[j]:
                count+=1
    if count%2==0:
        return count//2
    else:
        return (count-1)//2
    pass

s=sockMerchant(8, [10,20,20,30,40,10,90,10])
print(s)