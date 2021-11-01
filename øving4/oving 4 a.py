# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 14:38:41 2021

@author: LittleMe
"""

def getprice(a,b):
    if 18 <= a < 67:
        return(40)
    else:
        return(20)

    
    
    
    
age = int(input("Age: "))

price = getprice(age,45)  
  
print(price)


