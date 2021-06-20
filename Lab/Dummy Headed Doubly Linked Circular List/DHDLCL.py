# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 17:33:16 2021

@author: Meem
"""
from Node import Node as nd
class DoublyList:
# --------------------------Constructors----------------------------#    
    def __init__(self,a=list):
        contains_duplicates = any(a.count(element) > 1 for element in a)
        self.head=nd('X',None, None)
        tail=None
        if(contains_duplicates==False):
            for i in range(len(a)):
                new=nd(a[i], None, None)
                if self.head.next==None:
                    self.head.next=new
                    new.prev=new.next=self.head
                    self.head.prev=new
                    tail=new
                    # print(self.head.next.element)
                    
                else:
                    new.next=tail.next
                    new.prev=tail
                    tail.next=new
                    self.head.prev=new
                    tail=new
                    # print(tail.element)
        else:
                print("Linked list cannot be created, keys are not unique")
# --------------------------Basic Methods----------------------------#
    def showList(self):        
        n=self.head.next
        if(n==None):
            print("Empty List")
            return
        while n is not self.head:
            if n is not self.head:
                print(n.element)
            else:
                break
            n=n.next
    def nodeAt(self,index):
        n=self.head.next
        for i in range(0, index):
            n=n.next
        # print(n.element)
        return n
    def size(self):
        n=self.head.next
        s=0
        while n is not self.head:
            s+=1
            n=n.next
        return s
    def insert(self, newElement):
        n=self.head.next
        while n is not self.head:
            if n.element is newElement:
                print("Key already exists")
                return
            n=n.next
        new=nd(newElement, None, None)
        size=list1.size()
        g=list1.nodeAt(size-1)
        new.next=g.next
        g.next.prev=new
        g.next=new
        new.prev=g
            
        pass
    def insert1(self, newElement, index):
        n=self.head.next
        if(n==None):
            print("Empty List")
            return
        while n is not self.head:
            if n.element is newElement:
                print("Key already exists")
                return
            n=n.next
        new=nd(newElement, None, None)
        g=list1.nodeAt(index-1)
        new.next=g.next
        g.next.prev=new
        g.next=new
        new.prev=g
        pass
    def remove(self,index):
        n=self.head.next
        if n is None:
            print("Empty list")
            return
        remove=list1.nodeAt(index)
        remove.prev.next=remove.next
        remove.next.prev=remove.prev
        remove.next=remove.prev=remove=None
        pass
    def removeKey(self, deleteKey):
        n=self.head.next
        index=0
        if n is None:
            print("Empty List")
            return
        while n is not self.head:
            
            if n.element is not deleteKey:
                index+=1
            else:
                break
            n=n.next
        remove=list1.nodeAt(index)
        remove.prev.next=remove.next
        remove.next.prev=remove.prev
        remove.next=remove.prev=None
        deleteKeyVal=remove.element
        remove=None
        return deleteKeyVal
        pass
# --------------------------Tester Class----------------------------#   
list1=DoublyList([1,2,3,4,5])        #creates linked list
list1.insert(7)                  #inserts an element at the last index
list1.insert1(6,2)               #inserts element at the given index
list1.remove(2)                  #removes the key at given index
d=list1.removeKey(7)             #removes the key that matches the given and returns the deleted key value
list1.showList()                 #prints the list
print("deleted key value: ",d)   #prints the deleted key value from removeKey method