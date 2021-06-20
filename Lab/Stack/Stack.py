# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 23:05:58 2021

@author: Meem
"""
class Node:
    def __init__(self, val):
        self.value=val
        self.next=None
class StackArray:
    stack=[]
    pointer=-1
    def push(self, data):
        self.stack.append(data)
        self.pointer+=1
    def peek(self):
        if len(self.stack)==0:
            return None
        else:
            return self.stack[self.pointer]
    def pop(self):
        if len(self.stack)==0:
            return None
        value=self.stack[self.pointer]
        self.stack=self.stack[:-1]
        self.pointer-=1
        return value
    def checkParentheses(self, s):
        c=False
        exp=""
        index=0
        for i in s:
            index+=1
            if(i=="(" or i=="{" or i=="["):
                st.push(i)
            elif(i==")" or i=="}" or i=="]"):
                current=st.peek()
                exp=i
                if current is None:
                    c=False
                    break
                if i==")":
                    if current=="(":
                        c=True
                        st.pop()
                    else:
                        c=False
                        break
                if i=="}":
                    if current=="{":
                        c=True
                        st.pop()
                    else:
                        c=False
                        break
                if i=="]":
                    if current=="[":
                        c=True
                        st.pop()
                    else:
                        c=False
                        break
            else:
                continue
        if c==True:
            if(len(self.stack))==0:
                print ("This expression is correct")
                return
        elif c==False and st.peek()!=None:
                for i in range(len(s)):
                    if s[i]==st.peek():
                        index=i+1
                print("Error at character #",index,"'",st.peek(),"'","-not closed")
        else:
                print("Error at character #",index,"'",exp,"'","-not opened")
 
from Node import Node as nd
class StackLinkedList:
    head=None
    def push(self,data):
        if self.head is None:
            self.head=nd(data)
        else:
            n=nd(data)
            n.next=self.head
            self.head=n
    def peek(self):
        if self.head==None:
            return None
        else:
            return self.head.value
    def pop(self):
        temp=self.head
        self.head=self.head.next
        val=temp.value
        temp.value=temp.next=None
        return val
    def ParenthesesCheck(self,s):
        c=False
        exp=""
        index=0
        for i in s:
            index+=1
            if(i=="(" or i=="{" or i=="["):
                st1.push(i)
            elif(i==")" or i=="}" or i=="]"):
                current=st1.peek()
                exp=i
                if current is None:
                    c=False
                    break
                if i==")":
                    if current=="(":
                        c=True
                        st1.pop()
                    else:
                        c=False
                        break
                if i=="}":
                    if current=="{":
                        c=True
                        st1.pop()
                    else:
                        c=False
                        break
                if i=="]":
                    if current=="[":
                        c=True
                        st1.pop()
                    else:
                        c=False
                        break
            else:
                continue
        
                
        if c==True:
            if self.head is None:
                print ("This expression is correct")
                return
        elif c==False and st1.peek()!=None:
                
                for i in range(len(s)):
                    if s[i]==st1.peek():
                        index=i+1
                print("Error at character #",index,"'",st1.peek(),"'","-not closed")
        else:
                print("Error at character #",index,"'",exp,"'","-not opened")
                     

st=StackArray()
st1=StackLinkedList()
# s=input()              #commentout this line and comment the next line to take an input from the console
s="1+2]*[3*3+{4–5(6(7/8/9)+10)–11+(12*8)]+14" #string to evaluate
print(s)
st.checkParentheses(s) #Method in StackArray class to evaluate the string
print()
print(s)
st1.ParenthesesCheck(s) #Method in StackLinkedList class to evaluate the string