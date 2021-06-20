# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 12:02:44 2021

@author: Meem
"""

def Insert(self, newElement, index):
        n=self.head
        # print(element)
        # c=False
        count=0
        while n is not None:
            count=count+1
            if n.value is not newElement:
                new=nd(newElement,None)
                if count is index:
                    temp=n.next
                    n.next=new
                    new.next=temp
            else:
                break
            n=n.next
            
    def nodeAt(self, index):
        if(index<0):
            return None
        n = self.head
        for i in range(0,index):
            n = n.next
        return n
    
    def insert(head, size, elem, index):

        if(index<0 or index>size):

            raise Exception("Invalid index")

        newNode = nd(elem, None)

        if (index==0):

            newNode.next = head

            head = newNode

        else:

            pred = nodeAt(index-1)

            newNode.next = pred.next

            pred.next = newNode

        return head
def remove(head, size, index):

    if(index<0 or index>=size):

        raise Exception("Invalid index")

    removedNode = None

    if (index==0):

        removedNode = head

        head = head.next

    else:

        pred = nodeAt(index-1)

        removedNode = pred.next

        pred.next = removedNode.next

    removedNode.element = None

    removedNode.next = None

    return head



#indexOf Function

#------------------#

def indexOf(head, elem):

    i = 0

    n = head

    while n is not None:

        if n.element==elem:

            return i

        i = i + 1

        n = n.next

    return -1


def 

    def remove(self, deletekey):
        pass
    
list1=[1,2,3,4,5]
list2=MyList(list1)
list2.showList()
list6=MyList([1,2,5,3,8])
list6.sortList()
list6.showList()
list7=MyList([3,2,5,1,8])
list7.sumList()
list7.rotateList(2, False, True)
list7.showList()
# print(list2.isEmpty())
# list5=list2.evenNumbers()
# list2.elementExistence(7)
# list2.reverseList()
# list2.showList()
# list2.insert1(6)
# list2.showList()
# list2.insert(6, 3)
# list2.showList()
# print(list2.remove(6))
# list2.showList()
# list3=MyList(list2)
# list3.clear()
# list3.showList()
# list4=MyList()
# list4.showList()
# print(list4.isEmpty())