# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 00:38:20 2021

@author: Meem
"""

class Node(object):
    def __init__(self, value, next):
        self.value=value
        self.next=next
        
head=None

n4 = Node("40",None)

n3 = Node("30",n4)

n2 = Node("20",n3)

n1 = Node("10",n2)

head = n1

n=head

# while n is not None:
#     print(n.value,'->',n.next)
#     n=n.next