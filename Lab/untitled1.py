# -*- coding: utf-8 -*-
"""
Created on Sat May 22 15:34:57 2021

@author: Meem
"""

# def encodeWord(word,index,rand_num):
#     if index>=len(word):
#         return ""
#     else:
#         # word= str(chr(ord(word[index])+rand_num))
#         return str(chr(ord(word[index])+rand_num))+encodeWord(word,index+1,rand_num)
#     pass

# word="atef"
# rand_num=5
# print(encodeWord(word, 0, rand_num))

cost = [1.25, 3.00, 2.00, 4.75]
items = ["chocolate bar", "cone", "medium float", "ice cream sunday"]

print("Cost  -  Product")

i=0

for i in range(len(cost)):
    print(str(cost[i]) + " - " + items[i])