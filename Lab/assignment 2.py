# -*- coding: utf-8 -*-
"""
Created on Wed May 12 00:53:08 2021

@author: Meem
"""

# def exponential(m,n):
#     if n==0 or n==1:
#         return m
#     else:
#         return m*exponential(m,n-1)
#     pass

# print(exponential(3,2))
# class Trace:
#     def hMB(self,h):
#         if (h==0):
#             print("Stop: ",h)
#             return 0
#         elif(h==1):
#             print("Stop: ",h)
#             return h
#         else:
#             print("Continue: ",h)
#             return h + self.hMB(h-1)
# #Tester
# t = Trace()
# # t.hMB(5)
# print("Finally ",t.hMB(5))

# class Surprise:
#     def mystery(self,n):
#         print("h(" ,n,")")
#         if(n==0):
#             print("value: 0")
#             return 0
#         else:
#             print("going down")
#             temp = self.mystery(n-1)+1
#             print("h(",n,") --> ",temp)
#             return temp
# #Tester
# s = Surprise()
# s.mystery(4)

# class HouseOfCards:
# def hocBuilder(height):
#     if(height==0):
#         return height+3
#     elif(height==1):
#         return 8
#     elif(height>=1):
#         return 5+hocBuilder(height-1)
#     pass

# # h=HouseOfCards()
# h8=abs(int(input()))
# print(hocBuilder(h8))

# def printn(num):
     
#     # base case
#     if (num == 0):
#         return
#     print("1", end = " ")
 
#     # recursively calling printn()
#     printn(num - 1)
 
# # function to print the pattern
# def pattern(n, i):
     
#     # base case
#     if (n == 0):
#         return
#     printn(i)
#     print("\n", end = "")
     
#     # recursively calling pattern()
#     pattern(n - 1, i + 1)
 
# # Driver Code
# # if __name__ == '__main__':
# n = 5
# pattern(n, 1)

# def print_row(no, val):
     
#     # base case
#     if (no == 0):
#         return;
#     print(val , end=" ");
 
#     # recursively calling print_row()
#     print_row(no - 1, val);
 
# # function to print the pattern
# def pattern(n, num):
#     # base case
#     if (n == 0):
#         return;
#     print_row(num - n + 1, num - n + 1);
#     print("");
 
#     # recursively calling pattern()
#     pattern(n - 1, num);
 
# # Driver Code
# n = 5;
# pattern(n, n);

# function to print row
# def printRow(count,num):
# 	if num==0:
# 		return
# 	print(count,end=" ")
# 	printRow(count+1, num-1)
# 	return count
# def printPattern(n, count, num):
# 	if n==0:
# 		return
# 	count=printRow(count, num)
# 	print()
# 	printPattern(n-1,count,num+1)
# n = 5
# printPattern(n,1,1)


# def printSpace(space):
# 	if space==0:
# 		return
# 	print(" ", end=" ")
# 	printSpace(space - 1)

# def printRow(count,num):
# 	if num==0:
# 		return
# 	print(count,end=" ")
# 	printRow(count+1, num-1)
# 	return count

# def printPattern(n, count, num):
# 	if (n == 0):
# 		return
# 	printSpace(n-1)
# 	count=printRow(count,num-n+1)
# 	print()
# 	printPattern(n-1,count,num)

# n=5
# printPattern(n,1,n)

# class FinalQ:
#     def print(self,array,idx):
#         if(idx<len(array)):
#             profit = self.calcProfit(array[idx])
#             print("Investment:", array[idx],";","Profit:", profit)
#             #TO DO
#     def calcProfit(self,investment):
#         # remain er jonne 8 kore per 100 dollars e add hobe
#         # but tar ager 75k kintu 4.5 korei per 100 dollars e add hocche
#         # so what is going to happen is, amra jodi ekta condition dei jekhane hocche giye amra
#         # boltesi setup cost baad dewar por 75k porjnto 4.5 dollar per 100 e,
#         # ar oi baki jeta thakbe oitar upor 8 dollar
#         # Now here tmi shudhu investment pass korteso, so shudhu investment komate barate parba
#         # tahole ami jodi ber kori je investment e koyta 100 ase
#         # then oi jodi oi koita 8 add kori
#         # ar shathe investment choto korte thaki until 0 hoye jai
#         if investment<=0:
#             return 0
#         elif investment<=100000:
            
#             return 0.045+self.calcProfit()
#         #TO DO
#         pass
# #Tester
# array=[25000,100000,250000,350000]
# f = FinalQ()
# f.print(array,1)


# def arrayCompare(a, val):
#     print(val)
#     pass

# def sort(a,i):
#   length=len(a)
#   if i==length:
#     return -1
#   if i<length:
#     j=i-1
#     p=a[i]
#     while j>=0 and p<a[j]:
#       a[j+1]=a[j]
#       j=j-1
#     a[j+1]=p
#     sort(a,i+1)
#     pass

# a=[1, 1, 2, 2, 5]
# b=[3, 1, 4, 1, 5]
# sort(b,1)
# for i in range(len(b)):
#     val=b[i]
#     arrayCompare(a,val)

def arrayComparison(arr1,arr2):
	for i in range(len( arr2)):
		count=0
		for j in range(len( arr1)):
			if(arr1[j]>arr2[i]):
				break
			count+=1
		print(count, end=" ")
        
arr1=[1, 3, 5, 7, 9]
arr2=[6, 4, 8]
arrayComparison(0, arr2)