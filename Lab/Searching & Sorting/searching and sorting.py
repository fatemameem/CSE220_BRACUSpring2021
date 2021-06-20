# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 04:35:57 2021

@author: Meem
"""
# --------------------------Task 1----------------------------#
def recursiveSelectionSort(a,i,j):
  length=len(a)
  if i==length and j==length:
    return -1
  if i<length-1:
    m=i
    while j<length:
      if a[j]<a[m]:
        m=j
      j=j+1
    if m!= i:
      temp=a[i]
      a[i]=a[m]
      a[m]=temp
    recursiveSelectionSort(a,i+1,i+2)
A=[7,1,6,4,3,8]
recursiveSelectionSort(A,0,1)
print(A)

# --------------------------Task 2----------------------------#
def recursiveInsertionSort(a,i):
  length=len(a)
  if i==length:
    return -1
  if i<length:
    j=i-1
    p=a[i]
    while j>=0 and p<a[j]:
      a[j+1]=a[j]
      j=j-1
    a[j+1]=p
    recursiveInsertionSort(a,i+1)

A=[7,1,6,4,3,8]
recursiveInsertionSort(A,1)
print(A)

# --------------------------Singly Linked List Node----------------------------#
class SinglyNode(object):
    def __init__(self, value, next):
        self.value=value
        self.next=next
# --------------------------Singly Linked Sequential List----------------------------#
class SinglyLinkedList:
    head=None
# --------------------------Constructors----------------------------#
    def __init__(self,a=None):
        
        if(a==None):
            self.head=None
            
        elif isinstance(a, list):
                self.head=None
                tail=None
                for i in range(len(a)):
                    new=SinglyNode(a[i],None)
                    if self.head is None:
                        self.head=new
                        tail=new
                    else:
                        tail.next=new
                        tail=new
# --------------------------Basic Methods----------------------------#
    def showList(self):
        n=self.head
        if(n is None):
            print("Empty list")
        else: 
            while n is not None:
                if n.next is not None:
                    print(n.value,"->",end=" ")
                else:
                    print(n.value)
                n=n.next
                
# --------------------------Task 3----------------------------#
    def bubbleSort(self):   
        n=self.head;  
        i=None  
        if self.head is None:  
            return -1
        else:  
            while n is not None:
                i=n.next
                while i is not None:  
                    if(n.value>i.value):  
                        temp=n.value 
                        n.value=i.value  
                        i.value=temp  
                    i=i.next
                n=n.next
    def selectionSort(self):
        n=self.head
        while n is not None:
            m=n
            p=n.next
            while p is not None:
                if(m.value>p.value):
                    m=p
                p=p.next
            k=n.value
            n.value=m.value
            m.value=k
            n=n.next
            
list2=SinglyLinkedList([7,1,6,4,3,8])
list2.bubbleSort()
list2.showList()

# --------------------------Task 4----------------------------#
list3=SinglyLinkedList([7,1,6,4,3,8])
list3.selectionSort()
list3.showList()

# --------------------------Doubly Linked List Node----------------------------#
class DoublyNode:
    def __init__(self, e, n, p):
        self.element=e
        self.next=n
        self.prev=p

# --------------------------Doubly Linked Sequential List----------------------------#
class DoublyList:
# --------------------------Constructors----------------------------#    
    def __init__(self,a=list):
        self.head=None
        tail=None
        for i in range(len(a)):
                new=DoublyNode(a[i], None, None)
                if self.head==None:
                    self.head=new
                    new.prev=new.next=self.head
                    tail=new
                    
                else:
                    new.prev=tail
                    tail.next=new
                    tail=new
# --------------------------Basic Methods----------------------------#
    def showList(self):        
        n=self.head
        while n is not None:
            print(n.element)
            n=n.next
    def nodeAt(self,index):
        n=self.head
        for i in range(0, index):
            n=n.next
        # print(n.element)
        return n
# --------------------------Task 5----------------------------#
list1=DoublyList([1,2,3,4,5])
# list1.showList()

# --------------------------Task 6----------------------------#
def binarySearchRecursive(a,l,r,val):
    if r>=l:
        m=(r+l)// 2
        if a[m]==val:
            return m
        elif a[m]>val:
            return binarySearchRecursive(a,l,m-1,val)
        else:
            return binarySearchRecursive(a,m+1,r,val)
    else:
        return -1

a=[10,12,15,17,21,25,70,100]
left=0
right=len(a)-1
print(binarySearchRecursive(a,left,right,70))

# --------------------------Task 7----------------------------#

