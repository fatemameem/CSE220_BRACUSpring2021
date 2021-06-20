# -*- coding: utf-8 -*-
"""
Created on Sun May  2 04:34:21 2021

@author: Meem
"""

class KeyIndex:
    k=[]
# --------------------------Constructors----------------------------#
    def __init__(self, a=list):
        x=self.neg_index(a)
        for i in range(len(a)):
            a[i]=a[i]+x
        m=max(a)+1
        for i in range (m):
            self.k.append(0)
        for i in range(len(a)):
            self.k[a[i]]+=1
        # for i in range(len(self.k)):
        #     if(self.k[i]>=1):
        #         print(i)
# --------------------------Basic method----------------------------#    
    def neg_index(self,a):
        x=0
        if(min(a)<0):
           x=min(a)*-1
        return x
# --------------------------Methods for searching and sorting----------------------------#            
    def search(self,val):
        if(s.k[val] >= 1):
            return True
        elif (s.k[val]==0):
            return False
        pass
    def sort(self):
        # print(x)
        temp=[]
        i=0
        while i<len(self.k):
            j=1
            while j<=self.k[i]:
                temp.append(i)
                j+=1
            i+=1
        return temp
        pass
# --------------------------Tester----------------------------#
p=[4,-2,3,-4,7,4]
x=0
if(min(p)<0):
   x=min(p)*-1
s=KeyIndex(p)
value=int(input("Enter the value you want to search for: "))+x
print(s.search(value))
temp=s.sort()
for i in range(len(temp)):
    print(temp[i]-x)