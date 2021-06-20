# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 17:30:50 2021

@author: Meem
"""
# --------------------------Node Class----------------------------#
class Node:
    def __init__(self, e, n, p):
        self.element=e
        self.next=n
        self.prev=p