# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 13:49:14 2021

@author: Meem
"""

# comment out lines one by one to individually check them

from Node import Node as nd
import random as rd
class MyList:
    head=None
# --------------------------Constructors----------------------------#
    def __init__(self,a=None):
        
        if(a==None):
            self.head=None
            
        elif isinstance(a, list):
            # contains_duplicates = any(a.count(element) > 1 for element in a)
            # if(contains_duplicates==False):
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
            # else:
            #     print("Linked list cannot be created, keys are not unique")
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
                
# --------------------------Basic Methods----------------------------#
    
    def nodeAt(self, index):
        if(index<0):
            return None
        n = self.head
        for i in range(0,index):
            n = n.next
        return n
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
               
    def isEmpty(self):
        n=self.head
        if(n is None):
            return True
        else:
            return False
        
    def clear(self):
        while (self.head is not None):
            temp = self.head
            self.head = self.head.next
            temp = None
        print("All the elements of the list has been deleted")
        
    def insert1(self, newElement):
        n=self.head
        # print(element)
        # c=False
        while n is not None:
            if n.value is not newElement:
                new=nd(newElement,None)
                if n.next is None:
                    n.next=new
            else:
                break
            n=n.next
    def insert(self, newElement, index):
        n=self.head
        # i=index-1
        if(n==None):
            return "Empty List"
        c=False
        while n is not None:
            if(n.value==newElement):
                print("key already exists")
                c=True
            n=n.next
                
        if(c==False):
            new=nd(newElement, None)
            if(index<0):
                raise Exception("Invalid index")
            elif(index==0):
                new.next=self.head
                self.head=new
            elif(index>1):
                n = self.head
                for i in range(0,index-1):
                    n = n.next
                prev=n
                new.next=prev.next
                prev.next=new
            
    def remove(self, deleteKey):
        n=self.head
        if(n==None):
            return "Empty List"
        i=0
        index=0
        # deleteKeyValue=0
        while n is not None:
            if n.value==deleteKey:
                index=i
            i=i+1
            n=n.next
        removeNode=None
        if(index==0):
            # deleteKeyValue=self.head.value
            removeNode=self.head
            self.head=self.head.next
        elif(index>=1):
            n = self.head
            for i in range(0,index-1):
                n = n.next
            prev=n
            # deleteKeyValue=prev.next.value
            removeNode=prev.next
            prev.next=removeNode.next
        # return deleteKeyValue
    
# --------------------------Advanced Methods----------------------------#
    def evenNumbers(self):
        n=self.head
        even=[]
        while n is not None:
            if(n.value%2==0):
                even.append(n.value)
            n=n.next
        list1=MyList(even)
        i=list1.head 
        while i is not None:
            if i.next is not None:
                print(i.value,"->",end=" ")
            else:
                print(i.value)
            i=i.next
        pass
    
    def elementExistence(self, element):
        n=self.head
        c=True
        while n is not None:
            if(n.value==element):
                c=True
            else:
                c=False
            n=n.next
        print(c)
        pass
    
    def reverseList(self):
        newHead=None
        n=self.head
        while n is not None:
            nextNode=n.next
            n.next=newHead
            newHead=n
            n=nextNode
        self.head=newHead
        pass
    
    def sortList(self):   
        n=self.head;  
        i=None;  
        if n is None:
            print("Empty List")
            return 
        else:  
            while n is not None:  
                i=n.next;  
                while i is not None:  
                    if n.value>i.value:  
                        temp=n.value 
                        n.value=i.value;  
                        i.value=temp;  
                    i=i.next;  
                n=n.next;  
        pass
    
    def sumList(self):
        n=self.head
        listSum=0
        while n is not None:
            listSum+=n.value
            n=n.next
        print(listSum)
        pass
    
    def rotateList(self, k, left, right):
        if(left==True):
            for i in range(0,k):
                oldHead=self.head
                self.head=self.head.next
                tail=self.head
                while tail.next is not None:
                    tail=tail.next
                tail.next=oldHead
                oldHead.next=None
            
        elif(right==True):
            n=self.head
            size=1
            while n.next is not None:
                n=n.next
                size+=1
            if k>size:
                k=k%size
            k=size-k
            i=self.head
            count=1
            while count<k and i is not None:
                i=i.next
                count+=1
            if i is None:
                return
            kthnode=i
            n.next=self.head
            self.head=kthnode.next
            kthnode.next=None
        elif(right==False and left==False):
            return
    
# --------------------------Assignment-1----------------------------#
    # def printduplicate(self):
    #     count=0
    #     n=self.head
    #     while n is not None:
    #         temp=n.value
    #         p=n.next
    #         while p is not None:
    #             if p.value==temp:
    #                 print(p.value)
    #                 count=count+1
    #             p=p.next
    #         if(count==1):
    #             break
    #         n=n.next
    #     pass
    def removeNode(index):
        pass
    def remove_multiples_of_5(self,list1):
        n=list1.head
        # index=0
        temp=[]
        while n is not None:
            if (n.value%5==0):
                temp.append(n.value)
            n=n.next
        for i in range(len(temp)):
            list1.remove(temp[i])
        # print(temp)
        list1.showList()
        pass
    def musicalchair(self, participants, n):
        print("Begin: ",end="")
        participants.showList()
        while n>0:
            r=rd.randint(0, 3)
            if r==1:
                    pred=participants.nodeAt(int((n/2)-1))
                    remove=pred.next
                    pred.next=remove.next
                    remove.element=None
                    remove.next=None
                    participants.showList()
                    if n==1:
                        print("Winner:",end=" ")
                        participants.showList()
                        break
                    n=n-1
        pass
    def dummyListSum(dummyList,dummyList1):
        n=dummyList.head.next
        i=''
        while n is not None:
            i=i+str(n.value)
            n=n.next
            pass
        n=dummyList1.head.next
        i1=''
        while n is not None:
            i1=i1+str(n.value)
            n=n.next
            pass
        sum=int(i)+int(i1)
        # print(sum)
        # print(len(str(sum)))
        temp=[None]
        sum=str(sum)
        sum=sum[len(sum)::-1]
        for i in range(len(str(sum))):
            temp.append(int(sum)%10)
            sum=int(int(sum)/10)
        # print(temp)
        list2=MyList(temp)
        list2.showList()
        pass
    def insertBefore(self, element, newElement):
        n=self.head.next
        index=0
        while n is not None:
            index+=1
            if n.value is not element:
               n=n.next
            else:
                break
        new=nd(newElement, None)
        temp=self.nodeAt(index)
        before=temp.prev
        new.prev=before
        new.next=temp
        before.next=temp.prev=new
        
    
    # def insertElementCircular(self, element, index):
    #     n=self.head
    #     i=index-1
    #     count=0
    #     while n is not None:
    #         count+=1
    #         n=n.next
    #     n.next=self.head    
    #     new=nd(element, None)
    #     if(index<0):
    #         raise Exception("Invalid index")
    #     elif(index==0):
    #         new.next=self.head
    #         self.head=new
    #     elif(index>1 and index<count):
    #         n = self.head
    #         for i in range(0,index-1):
    #                n = n.next
    #         prev=n
    #         new.next=prev.next
    #         prev.next=new
    #     elif(index>=count):
    #         n=self.head
    #         for i in range(0,count):
    #             n=n.next
    #         tail=n
    #         new.next=tail.next
    #         tail.next=new
                # pass
# --------------------------HackerRank Practice----------------------------#
    def getNode(self, positionFromTail):
        newHead=None
        n=self.head
        while n is not None:
            nextNode=n.next
            n.next=newHead
            newHead=n
            n=nextNode
        self.head=newHead
        n=self.head 
        for i in range(0,positionFromTail):
            n=n.next
        print(n.value)
        pass
    
    def insertNodeAtHead(self, data):
        n=self.head
        new=nd(data, None)
        new.next=n
        self.head=new
        pass

# --------------------------Recursion----------------------------#

    def sumNodes(self):
        if self.head is None:
            return None
        else:
            return self.head.value+list11.sumNodes(self.head.next)

# --------------------------Tester Class----------------------------#
list11=MyList([1,2,8,9,15])
list11.sumNodes()
# list10=MyList([1,2,3,4,5,6])
# list10.insert1(7)
# list10.showList()
# list10.getNode(2)
# circularList=MyList([1,2,3,4,5])
# circularList.insertElementCircular(6, 5)
# circularList.showList()
# dummyList=MyList([None,4,5,3])
# dummyList1=MyList([None,9,5,2])
# MyList.dummyListSum(dummyList,dummyList1)
# p=['A','B','C','D','E','F','G']
# participants=MyList(p)
# n=len(p)-1
# # print(n)
# participants.musicalchair(participants,n)
# list10=MyList([1,2,3,3,4,5,6,6])
# list10.printduplicate()
# list11=MyList([10,5,9,6,30,25])
# list11.remove_multiples_of_5(list11)
# list1=MyList()
# list2=MyList([1,2,3,4,5])
# list3=MyList(list2)
# list1.showList()
# list2.showList()
# list3.showList()
# print(list1.isEmpty())
# print(list2.isEmpty())
# list3.clear()
# list3.showList()
# list2.insert1(6)
# list2.showList()
# list2.insert(7, 3)
# list2.showList()
# list2.remove(7)
# list2.showList()
# list4=MyList([1,2,5,3,8])
# list4.evenNumbers()
# list4.elementExistence(7)
# list5=MyList(list4)
# list5.reverseList()
# list5.showList()
# list6=MyList(list4)
# list6.sortList()
# list6.showList()
# list4.sumList()
# list7=MyList([3,2,5,1,8])
# list8=MyList(list7)
# list7.rotateList(2, True, False)
# list7.showList()
# list8.rotateList(2, False, True)
# list8.showList()
