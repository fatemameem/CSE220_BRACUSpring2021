# -*- coding: utf-8 -*-
"""
Created on Fri May 21 02:50:49 2021

@author: Meem
"""

x=[10,1,20,3,6,2,5,11,15,2,12,14,17,18,29]

 

for i in range(0, len(x)):

    m = x[i]

    l = i

 

# Finding the minimum value and its location

    for j in range(i+1, len(x)):

        if(m >x [j]):

            m= x[j]

            l = j

# Now we will do the swapping

    tmpry = m

    x[l] = x[i]

    x[i] = tmpry

 

print(x)