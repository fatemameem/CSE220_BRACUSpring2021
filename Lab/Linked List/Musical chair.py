# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 18:49:11 2021

@author: Meem
"""

import Node as nd
class Musical chai:
# --------------------------Constructors----------------------------#
    def __init__(self,a=None):
        
        if(a==None):
            self.head=None
            
        elif isinstance(a, list):
            contains_duplicates = any(a.count(element) > 1 for element in a)
            if(contains_duplicates==False):
                self.head=None
                tail=None
                for i in range(len(a)):
                # print(a[i])
                    new=nd(a[i],None)
                # print(new.value)
                    if self.head is None:
                        self.head=new
                        tail=new
                    # print(self.head)
                    else:
                        tail.next=new
                        tail=new
            else:
                print("Linked list cannot be created, keys are not unique")
        elif isinstance(a, MyList):
            self.head=None
            tail=None
            n=a.head
            while n is not None:
                new=nd(n.value,None)
                if self.head is None:
                    self.head=new
                    tail=new
                else:
                    tail.next=new
                    tail=new
                n=n.next

p=['A','B','C','D','E','F','G']
participants=MyList(p)
n=len(p)
print(n)