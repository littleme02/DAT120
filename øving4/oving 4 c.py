# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 09:52:38 2021

@author: Little-think
"""


try:
    a = int(input("Age: "))
      
    if a < 0:
        print("Invalid")
    elif(18 <= a < 67):
        print("40")
    else:
        print("20")
        
except: print("Error")