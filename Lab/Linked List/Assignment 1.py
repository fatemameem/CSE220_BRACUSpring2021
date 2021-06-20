# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 00:34:45 2021

@author: Meem
"""

class Node:
    def __init__(self,e,n,p):
        self.element = e
        self.next = n
        self.prev = p
def insertAfter(self,p, elem):
    n = Node (elem, None, None)
    q = p.next
    n.next = q
    n.prev = p
    p.next = n
    q.prev = n
    return n
head = Node(None,None,None)
head.next = head.prev = head
n = Node("hello", None, None)
n.next = head.next
n.prev = head
head.next = n
n.next.prev = n

