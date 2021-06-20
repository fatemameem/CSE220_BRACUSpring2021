# -*- coding: utf-8 -*-
"""
Created on Mon May 10 02:25:39 2021

@author: Meem
"""
# --------------------------Hashtable functions----------------------------#
def hashFunction(text):
    consonants = "BCDFGHJKLMNPQRSTVWXYZ"
    digits="0123456789"
    count = 0
    for x in text:
        if x in consonants:
            count += 1
    # print(count)
    s=0
    for x in text:
        if x in digits:
            s+=int(x)
    # print(s)
    return (count*24+s)%9

def linearProbing(a,i,aux,index):
    if(aux[index] is None):
        aux[index]=a[i]
        return
    elif(aux[index] is not None):
        return linearProbing(a,i,aux,index+1)
    pass

def hashTable(a):
    aux=[None]*len(a)
    for i in range(len(a)):
        index=hashFunction(a[i])
        print(a[i],index)
        linearProbing(a,i,aux,index)
    return aux
    pass


# --------------------------Tester----------------------------#
A=["JZFE9FP6XU","ST1E89B8A32","2JPNJ4I6KX","Z6ITCKJXXR",
   "AGJHOKNTA2","6MV24QCZ3W","4Z0KEJ5XCC","MZBGG8ESRL",
   "7O855A0XA5","82Y1SJAAGR"]
table=hashTable(A)
for i in range(len(table)):
    print(i,": ",table[i])
