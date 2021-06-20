# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 01:07:01 2021

@author: Meem
"""

def factorial(n):
    if n==1:
        return n
    else:
        return n*factorial(n-1)
    pass

def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
    pass

def printArray(a,i):
    if i==len(a):
        return None
    else:
        print(a[i])
        printArray(a,i+1)
    pass

def decimalToBinary(n):
    if n==0:
        return 0
    else:
        return n%2+10*(int(decimalToBinary(n/2)))
    pass

def exponential(m,n):
    if n==0 or n==1:
        return m
    else:
        return m*exponential(m,n-1)
    pass

def superDigit(n,k):
    def sumDigit(v):
        if v<10:
            return v
        s= sum(int(i) for i in str(v))
        return  sumDigit(s)
    x=sumDigit(int(n))
    return sumDigit(x*k)
    pass

print(superDigit("9875", 4))
# print(factorial(4))
# print(fibonacci(9))
# a=[1,2,3,4,5]
# printArray(a,0)
# print(decimalToBinary(5))
# print(exponential(2,8))
# if (len(n)==0):
#         return k
#     else:
#         k=int(n[-1])+k
#         return superDigit(n[:-1],k)